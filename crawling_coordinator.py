import city_crawler
from data_loader import DataCacher
from utils import chunks


def retrieve_results_for_city(cacher: DataCacher, city_id: int, batch_size:int=20):
    """
    :param cacher: python object that will store data from the file
    :param city_id: the city id - for example Petakh Tikva is 7900
    :param batch_size: number of ids in one batch
    :return:
    """
    city_ids = cacher.get_ids()[city_id]
    city_id_filtered = [id for id in city_ids if not cacher.is_item_in_results(id)]
    chunked_ids = chunks(city_id_filtered, batch_size)
    num_of_batches = len(city_id_filtered) // batch_size + 1
    print(f"total of {cacher.get_item_results_total_length()} item results")
    print(f"processing {num_of_batches} batches of size {batch_size}, total of {len(city_id_filtered)} ids. ")
    for e, batch in enumerate(chunked_ids):
        print(f"batch {e} of {num_of_batches}")
        results = city_crawler.get_item_by_list_ids(batch)
        cacher.add_item_results(results)
        cacher.save_state()

import tqdm
import time

def retrieve_ids_for_city(cacher:DataCacher, city_id:int, page_limit:int=100):
    print(len(cacher.get_ids_city(7900)))
    saved_ids = set(cacher.get_ids_city(city_id))
    print(f"currently there are {len(saved_ids)} saved ids for city {city_id}")
    for page in tqdm.tqdm(range(1, page_limit + 1)):
        ids_in_page = city_crawler.get_ids_for_city(page, city_id, True)
        new_ids_count = 0
        ids_to_add = set()
        for id in ids_in_page:
            if id in saved_ids:
                continue
            else:
                new_ids_count+=1
                ids_to_add.add(id)
                saved_ids.add(id)

        time.sleep(1)
        print(f"found {len(ids_to_add)} new ids in page {page}. total: {len(ids_in_page)} ids")
        cacher.add_ids(city_id,ids_to_add)
        cacher.save_state()

cacher = DataCacher()
retrieve_results_for_city(cacher, 7900)
# retrieve_ids_for_city(cacher,7900)


