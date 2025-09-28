from flask import Flask
import pymongo
from pymongo.mongo_client import MongoClient
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Azure App Service! (deployed from github) :) 🚀"

@app.route("/testdb")
def testdb():
        # --- Replace these variables with your information ---
    # It's highly recommended to use a .env file for storing sensitive credentials.
    # Replace '<YOUR_CONNECTION_STRING>' with your actual connection string from the Azure portal.
    CONNECTION_STRING = os.getenv("AZURE_COSMOS_CONNECTIONSTRING")
    
    DATABASE_NAME = "your_database_name"
    COLLECTION_NAME = "your_collection_name"
    
    # --- Connect to Azure Cosmos DB for MongoDB ---
    try:
        # Set the TLS/SSL options required by Cosmos DB.
        client = MongoClient(CONNECTION_STRING, tls=True, tlsAllowInvalidCertificates=True)
    
        # Validate the connection by checking server info
        client.server_info()
        print("Successfully connected to Azure Cosmos DB for MongoDB.")
    
        # Access the specified database and collection
        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]
    
        # --- Print all documents in the collection ---
        print(f"\n--- Printing all documents in collection '{COLLECTION_NAME}' ---")
        
        # Use find() to get all documents.
        # The result is a cursor, so iterate over it to print each document.
        for document in collection.find():
            print(document)

        return "success - reading from cosmos"
    
    except pymongo.errors.ConnectionFailure as e:
        print(f"Failed to connect to Cosmos DB: {e}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # --- Close the connection ---
        if 'client' in locals() and client:
            client.close()
            print("\nConnection to Cosmos DB closed.")

@app.route("/mongodb")
def testmongodb():
        # --- Replace these variables with your information ---
    # It's highly recommended to use a .env file for storing sensitive credentials.
    # Replace '<YOUR_CONNECTION_STRING>' with your actual connection string from the Azure portal.
    CONNECTION_STRING = os.getenv("AZURE_COSMOS_CONNECTIONSTRING")
    
    DATABASE_NAME = "webappwithdb1-database"
    COLLECTION_NAME = "prjcollection"
    
    # --- Connect to Azure Cosmos DB for MongoDB ---
    try:
        # Set the TLS/SSL options required by Cosmos DB.
        client = MongoClient(CONNECTION_STRING, tls=True, tlsAllowInvalidCertificates=True)
    
        # Validate the connection by checking server info
        client.server_info()
        print("Successfully connected to Azure Cosmos DB for MongoDB.")
    
        # Access the specified database and collection
        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]

        doc = {
            "_id": str(uuid.uuid4()),   # generate a unique id
            "city": "Toronto",          # must match your partition key
            "name": "Test Document"
        }
        
        try:
            result = collection.insert_one(doc)
            print(f"Inserted document with _id: {result.inserted_id}")
        except Exception as e:
            print(f"Error inserting document: {e}")
    
        # --- Print all documents in the collection ---
        print(f"\n--- Printing all documents in collection '{COLLECTION_NAME}' ---")
        
        # Use find() to get all documents.
        # The result is a cursor, so iterate over it to print each document.
        for document in collection.find():
            print(document)

        return "success - reading from cosmos"
    
    except pymongo.errors.ConnectionFailure as e:
        print(f"Failed to connect to Cosmos DB: {e}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # --- Close the connection ---
        if 'client' in locals() and client:
            client.close()
            print("\nConnection to Cosmos DB closed.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
