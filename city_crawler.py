import re

import bs4
import requests
import time

def get_items_for_city(page:int=1, city_id:int=7900, verbose:bool=False):
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

    return results

def get_all_item_ids(city_id:int=7900, limit:int=100):
    id_list = []
    for page in range(1,limit+1):
        ids_in_page = get_items_for_city(page, city_id)
        id_list.extend(ids_in_page)
        time.sleep(1)

    print(f"found {id_list} ids")
    return id_list
