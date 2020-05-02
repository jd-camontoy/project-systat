import os
import pymongo

class Storage:
    def get_collection(collection_name):
        host = os.getenv('DB_HOST')
        port = int(os.getenv('DB_PORT'))
        database_name = os.getenv('DB_NAME')
        mongodb_client = pymongo.MongoClient(host, port)
        database = mongodb_client[database_name]
        collection = database[collection_name]
        return collection
