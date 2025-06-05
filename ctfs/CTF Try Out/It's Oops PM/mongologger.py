from typing import Any

MONGO_CSTR="mongodb://localhost:27017/"
import pymongo


class MongoLogger():
    def __init__(self, dbname, colname):
        self.client = pymongo.MongoClient(MONGO_CSTR)
        self.db = self.client[dbname]
        self.col = self.db[colname]

    def log(self, msg: dict):
        self.col.insert_one(msg)

    def get_latest_entry(self):
        result = self.col.find_one(
            dict(),
            sort=[( '_id', pymongo.DESCENDING )]
        )
        return result


    def do_we_have_i(self, i: int) -> bool:
        """
        Did we already send `i` to the endpoint?
        """
        result = self.col.find_one(
            {"i (int)": i}
        )

        return result is not None

if __name__ == "__main__":
    ml = MongoLogger()

    ml.log({"test": "This is a test message"})
    print(ml.get_latest_entry())
