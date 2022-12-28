
from pymongo import MongoClient

def get_database():
   CONNECTION_STRING = "localhost:27017"
   client = MongoClient(CONNECTION_STRING)

   return client['cbir']

if __name__ == "__main__":
   # Get the database
   dbname = get_database()