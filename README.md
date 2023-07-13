
# MongoDB-PythonConnection: A Hands-on Guide

## Introduction
MongoDB-PythonConnection is a concise, straightforward guide to setting up a connection with a MongoDB database, executing write operations, and reading the data, all from Python. In just 30 lines of Python code, you'll be able to establish a connection to your database, write profiles of three individuals, and read the results back.

This guide provides a simple, effective way to practice connecting, writing, and reading from a MongoDB database using Python. The concept is to use the PyMongo module in Python to demonstrate database operations.

## Key Features
* **Easy Connection**: Uses `pymongo.MongoClient` to connect to your MongoDB database.
* **Data Writing**: Demonstrates how to insert multiple documents into your MongoDB database.
* **Data Reading**: Shows you how to retrieve and print all documents from your MongoDB collection.

## Prerequisites
* Python 3.x installed on your machine.
* PyMongo module installed on your Python environment.
* Access to a MongoDB database.


```
from pymongo import MongoClient

uri = 'mongodb+srv://tosniki91:N25kbverb@clustervkapture.b6tox4s.mongodb.net'
password = 'N25kbverb'

client = MongoClient(uri, password=password)
db = client.sample_mflix
collection = db.comments

print("Executing query...")  # Добавленная инструкция для вывода

result = collection.find_one({"key": "value"})
print(result)


# Вы можете использовать переменную "db" для выполнения операций с базой данных, например:
collection = db.comments
result = collection.find({"key": "value"})
for document in result:
    print(document)
```

## How to Run
Ensure you have met all prerequisites before proceeding. 

1. Clone the repository on your local machine.
2. Update the database URI in the script with your MongoDB database URI.
3. Run the script.

## Running with Docker
To run the MongoDB-PythonConnection script inside a Docker container, follow these steps:

1. Build the Docker image from the Dockerfile in the project.
   ```
   docker build -t mongodb-pythonconnection .
   ```
2. Run the Docker container from the image.
   ```
   docker run mongodb-pythonconnection
   ```
3. Make sure to adjust the MongoDB URI to point to a reachable MongoDB instance.

## Conclusion
With MongoDB-PythonConnection, connecting, writing, and reading from a MongoDB database has never been easier. Whether you're a beginner seeking to understand database operations or an experienced developer looking for a quick refresher, this guide will prove to be an invaluable resource. Get started today and master MongoDB operations using Python!

**Disclaimer**: It's important to remember to keep sensitive information like your MongoDB URI private and secure.
