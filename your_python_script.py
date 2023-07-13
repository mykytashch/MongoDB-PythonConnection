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
