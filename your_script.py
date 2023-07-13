from pymongo import MongoClient

# Создайте нового клиента и подключитесь к серверу
client = MongoClient('mongodb+srv://tosniki91:N25kbverb@clustervkapture.b6tox4s.mongodb.net/')

# Отправьте пинг, чтобы подтвердить успешное подключение
try:
    client.admin.command('ping')
    print("Пинговали вашу базу данных. Успешное подключение к MongoDB!")
except Exception as e:
    print(e)

# Выберите базу данных (она будет создана при вставке первого документа)
db = client['my_database']

# Выберите коллекцию (она тоже будет создана при вставке первого документа)
collection = db['my_collection']

# Создайте несколько документов
docs = [{"name": "John", "age": 30, "city": "New York"},
        {"name": "Jane", "age": 25, "city": "Chicago"},
        {"name": "Jim", "age": 35, "city": "Los Angeles"}]

# Вставьте документы в коллекцию
collection.insert_many(docs)

# Выведите все документы из коллекции
for doc in collection.find():
    print(doc)
