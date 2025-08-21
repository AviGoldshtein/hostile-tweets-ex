from pymongo import MongoClient

class Fetcher:
    def __init__(self, user="IRGC", password="iraniraniran", database_name="IranMalDB", collection_name="tweets"):
        self.client = None
        self.db = None
        self.user = user
        self.password = password
        self.database_name = database_name
        self.collection_name = collection_name

    def get_collection_data(self):
        uri = f"mongodb+srv://{self.user}:{self.password}@{self.database_name}.gurutam.mongodb.net/"
        with MongoClient(uri) as client:
            self.db = client[self.database_name]
            collection = self.db[self.collection_name]
            result = list(collection.find({}))
            return result
