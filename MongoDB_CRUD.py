from pymongo import MongoClient
from bson.objectid import ObjectId

# This is a class for performing CRUD operations on the any database collection in MongoDB in tandem with Jupyter Notebook.
# NOTE: Module 4 guidance was provided by SNHU professor Dr. Steve Satterfield's video: https://www.youtube.com/watch?v=WwPc-0jWCBw.

class CRUD_Operations(object):
    """ CRUD operations for a database collection in MongoDB """

    def __init__(self, username, password, host, port, db_name, collection_name):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # Variables are not hardcoded, but passed as
        # parameters for Jupyter Notebook (where the data
        # is stored in a separate file) to use.
   
        #
        # Connection Variables
        #
        self.USER = username
        self.PASS = password
        self.HOST = host
        self.PORT = port
        self.DB = db_name
        self.COL = collection_name

        #
        # Initialize Connection
        # NOTE: I changed all variables to self.VARIABLE per a compiler warning.
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (self.USER, self.PASS, self.HOST, self.PORT))
        self.database = self.client[self.DB]
        self.collection = self.database[self.COL]

# Implement the C in CRUD. Return success or failure as Boolean values.
    def create(self, data):
        if isinstance(data, dict) and data:  # Check if 'data' is a dictionary and not empty.
            try:
                result = self.collection.insert_one(data)
                return True if result.inserted_id else False
            except Exception as e:
                print(f"An error occurred while inserting data: {e}")
                return False
        else:
            raise Exception("Nothing to save, because the data isn't correctly formatted.")

# Implement the R in CRUD. Manually assign a cursor (MongoDB tool for iterating over large datasets) to the query result.
    def read(self, query):
        if isinstance(query, dict):  # Check if 'query' is a dictionary.
            try:
                cursor = self.collection.find(query) 
                return list(cursor)  # Return 'cursor' as a list of documents if the command is successful.
            except Exception as e:
                print(f"An error occurred while querying documents: {e}")
                return []  # Return an empty list if the command is unsuccessful.
        else:
            raise Exception("Nothing to read, because the query isn't correctly formatted.")
        
# Implement the U in CRUD. Return the number of objects modified in the collection.
    def update(self, query, new_values):
        if isinstance(query, dict) and query and isinstance(new_values, dict) and new_values:  # Check if 'query' and 'new_values' are dictionaries and not empty.
            try:
                result = self.collection.update_many(query, {"$set": new_values})  # Use $set operator to update the fields in the documents.
                return result.modified_count  # Return the number of documents modified.
            except Exception as e:
                print(f"An error occurred while updating documents: {e}")
                return 0  # If the command is unsuccessful, 0 documents have been modified.
        else:
            raise Exception("Nothing to update, because one or both of the queries aren't correctly formatted.")

# Implement the D in CRUD. Return the number of objects removed from the collection.
    def delete(self, query):
        if isinstance(query, dict) and query:  # Check if 'query' is a dictionary and not empty.
            try:
                result = self.collection.delete_many(query)  # Delete all documents matching the query.
                return result.deleted_count  # Return the number of documents deleted.
            except Exception as e:
                print(f"An error occurred while deleting documents: {e}")
                return 0  # If the command is unsuccessful, 0 documents have been deleted.
        else:
            raise Exception("Nothing to delete, because the query isn't correctly formatted.")
        
