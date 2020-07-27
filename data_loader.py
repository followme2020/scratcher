import os
import pickle

PICKLE_NAME = "data_cache.obj"

class DataCacher:
    def __init__(self, filename:str=PICKLE_NAME):
        self.ids = {}
        self.item_results = {}
        self.filename = filename
        if (os.path.exists(filename)):
            with open(filename, 'rb') as f:
                datacache = pickle.load(f)
                self.ids = datacache.ids
                self.item_results = datacache.item_results

    def save_state(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self, f)

    def add_ids(self, city:int, ids: list):
        if city not in self.ids.keys():
            self.ids[city] = ids
        else:
            self.ids[city].extend(ids)

    def get_ids(self):
        return self.ids

    def add_item_results(self, results:dict):
        for k,v in results.items():
            if k not in self.item_results.keys():
                self.item_results[k] = v

    def get_item_results(self):
        return self.item_results

    def get_ids_total_length(self):
        count = 0
        for k,v in self.ids.items():
            count+=len(self.ids[k])
        return count

    def get_ids_length_for_city(self, city:int):
        if city in self.ids.keys():
            return self.ids[city]
        return 0