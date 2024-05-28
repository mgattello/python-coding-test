import csv

class DataCache:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.cache = None

    def load_data(self):
        with open(self.csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            self.cache = list(reader)

    def get_data(self):
        if self.cache is None:
            self.load_data()
        return self.cache

    def clear_cache(self):
        self.cache = None
