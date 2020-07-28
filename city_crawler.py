import re
import time
import bs4
import requests
import tqdm

def get_ids_for_city(page:int=1, city_id:int=7900, verbose:bool=False):
    """
    :param page: the page number to extract the items from
    :param city_id: the city id - for example Petakh Tikva is 7900
    :param verbose: choose whether to print the found ids and the match number
    :return: list of all the item ids on the specific page - for example - ['wokcob', 'keqxe0', '06mp98', '9njbjv', ... ]
    """
    res = requests.get(f'https://www.yad2.co.il/realestate/forsale?city={city_id}&page={page}')
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    blocks = soup.select('.feeditem.table')
    pattern = r'item-id=\"......\"'
    matches = re.finditer(pattern, str(blocks), re.MULTILINE)
    results = []
    for matchNum, match in enumerate(matches, start=1):
        if (verbose):
            print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                                end=match.end(), match=match.group()))
        results.append(match.group()[9:-1])

    return set(results)

def get_all_ids_city(city_id:int=7900, limit:int=100, page_sleep_interval:int=1, verbose:bool=True):
    id_list = []
    for page in tqdm.tqdm(range(1,limit+1)):
        ids_in_page = get_ids_for_city(page, city_id, True)
        id_list.extend(ids_in_page)
        time.sleep(page_sleep_interval)
        if (verbose):
            print(f"page {page}: found: {len(ids_in_page)} ids. result: {ids_in_page}")

    if (verbose):
        print(f"found {len(id_list)} ids in total")

    return set(id_list)

def get_item_by_id(item_id:str):
    api_link = f'https://www.yad2.co.il/api/item/{item_id}'
    response = requests.get(api_link)
    result = response.json()
    return result

# TODO: Optimize method for multiple async calls
def get_item_by_list_ids (item_list:list, sleep_interval_sec:int=1):
    results = {}
    for i in tqdm.tqdm(item_list):
        try:
            results[i] = get_item_by_id(i)
            time.sleep(sleep_interval_sec)
        except Exception as e:
            print(f"Unable to get item: {i}")
    return results
