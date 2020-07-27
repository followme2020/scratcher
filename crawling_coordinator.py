
import city_crawler
from data_loader import DataCacher

cacher = DataCacher()
print(cacher.get_ids())
print(cacher.get_ids_total_length())
# result  = city_crawler.get_items_for_city(2,7900,True)
# result  = city_crawler.get_all_ids_city(7900,10)
# print(result)
# cacher.add_ids(7900,result)
# cacher.save_state()
print(cacher.get_ids())
#
