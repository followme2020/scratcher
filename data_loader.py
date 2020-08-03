import os
import pickle

PICKLE_NAME = "data_cache.obj"

class DataCacher:
    def __init__(self, filename: str = PICKLE_NAME):
        """
        :param filename: the file name that will store the data, if file allready exist, this __init__
        method cache data for not over righting)
        """
        self.ids = {}
        self.item_results = {}
        self.filename = filename
        if (os.path.exists(filename)):
            with open(filename, 'rb') as f:
                datacache = pickle.load(f)
                self.ids = datacache.ids
                self.item_results = datacache.item_results

    def save_state(self):
        """
        :return:save current information to a file
        """
        with open(self.filename, 'wb') as f:
            pickle.dump(self, f)

    def add_ids(self, city: int, ids: set):
        """
        :param city:the city id - for example Petakh Tikva is 7900
        :param ids: for example - ['wokcob', 'keqxe0', '06mp98', '9njbjv', ... ]
        :return: updated list of ids
        """
        if city not in self.ids.keys():
            self.ids[city] = ids
        else:
            self.ids[city].update(ids)

    def get_ids(self):
        return self.ids

    def get_ids_city(self, city_id:int):
        return self.ids[city_id]

    def add_item_results(self, results: dict):
        for k, v in results.items():
            if k not in self.item_results.keys():
                self.item_results[k] = v

    def is_item_in_results(self, key: str):
        return key in self.item_results.keys()

    def get_item_results(self):
        return self.item_results

    def get_item_results_total_length(self):
        return len(self.item_results)


    def get_ids_total_length(self):
        count = 0
        for k, v in self.ids.items():
            count += len(self.ids[k])
        return count

    def get_ids_length_for_city(self, city: int):
        if city in self.ids.keys():
            return self.ids[city]
        return 0
