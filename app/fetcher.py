from pymongo import MongoClient
import os

class Fetcher:
    def __init__(self, collection_name="tweets"):
        self.client = None
        self.db = None
        self.user = os.getenv("MONGO_USER")
        self.password = os.getenv("MONGO_PASSWORD")
        self.database_name = os.getenv("MONGO_DATABASE")
        self.collection_name = collection_name

    def get_collection_data(self):
        uri = f"mongodb+srv://{self.user}:{self.password}@{self.database_name}.gurutam.mongodb.net/"
        with MongoClient(uri) as client:
            self.db = client[self.database_name]
            collection = self.db[self.collection_name]
            result = list(collection.find({}, {"TweetID": 0}))
            return result
