MONGO_CSTR="mongodb://localhost:27017/"
import pymongo


class MongoLogger():
    def __init__(self):
        self.client = pymongo.MongoClient(MONGO_CSTR)
        self.db = self.client["itsoopspm"]
        self.col = self.db['tcp_dump']

    def log(self, msg: dict):
        self.col.insert_one(msg)

    def print_latest_entry(self):
        result = self.col.find_one(
            dict(),
            sort=[( '_id', pymongo.DESCENDING )]
        )
        return result

if __name__ == "__main__":
    ml = MongoLogger()

    print(ml.print_latest_entry())
