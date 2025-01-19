import os

from fastapi import FastAPI, HTTPException
from pymongo import MongoClient

mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
mongo_client = MongoClient(mongo_uri)
db = mongo_client["example_db"]
collection = db["example_collection"]

app = FastAPI()


@app.get("/")
def read_root(insert=None):
    try:
        if insert is not None:
            # Insert the data if it's provided in the query parameter
            collection.insert_one({"data": insert})
            return {"message": f"Data {insert} added successfully"}
        else:
            # Otherwise, return all documents from the collection
            return list(collection.find({}, {"_id": 0}))
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
