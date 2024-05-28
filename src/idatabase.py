from src.idata_cache import DataCache
from src.utils import prepare_key

class IDatabase(DataCache):
    def __init__(self):
        super().__init__('data/database.csv')
    
    def query_db(self, value):
        for obj in super().get_data():
            if(obj["Company Name"] == value):
                for k,v in list(obj.items()):
                    key = prepare_key(k)
                    obj[key] = str(v)
                    del obj[k]
                return obj
