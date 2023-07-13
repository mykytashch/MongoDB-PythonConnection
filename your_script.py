from pymongo import MongoClient
client = MongoClient('mongodb+srv://tosniki91:password@clustervkapture.b6tox4s.mongodb.net/')
try:
    client.admin.command('ping')
    print("Пинговали вашу базу данных. Успешное подключение к MongoDB!")
except Exception as e:
    print(e)
db = client['my_database']
collection = db['my_collection']
docs = [{"name": "John", "age": 30, "city": "New York"},
        {"name": "Jane", "age": 25, "city": "Chicago"},
        {"name": "Jim", "age": 35, "city": "Los Angeles"}]
collection.insert_many(docs)
for doc in collection.find():
    print(doc)