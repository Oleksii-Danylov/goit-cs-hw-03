from pymongo import MongoClient
from pymongo.errors import PyMongoError, ConnectionFailure

try:
    client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=5000)
    client.admin.command('ping') 
    db = client["cats_database"]
    collection = db["Home"]
    print("MongoDB підключено успішно")
except ConnectionFailure:
    print("Помилка: не вдалося підключитися до MongoDB. Перевірте, чи запущений сервер!")
except Exception as e:
    print(f"Інша помилка: {e}")


def create_document():
    try:
        name = input("Введіть ім'я тварини: ")
        age = int(input("Введіть вік тварини: "))
        features_input = input("Введіть особливості тварини, розділені комою: ")
        features = features_input.split(", ")
        document = {"name": name, "age": age, "features": features}
        collection.insert_one(document)
        print("Документ створено.")

    except PyMongoError as e:
        print(f"Помилка при роботі з MongoDB: {e}")
    except ValueError as e:
        print(f"Помилка введення: {e}")

def read_all_documents():
    try:
        documents = collection.find()
        for doc in documents:
            print(doc)
    except PyMongoError as e:
        print(f"Помилка при зчитуванні: {e}")

def read_document_by_name():
    try:
        name = input("Введіть ім'я тварини: ")
        document = collection.find_one({"name": name})
        if document:
            print(document)
        else:
            print("Документ не знайдено.")
    except PyMongoError as e:
        print(f"Помилка при зчитуванні: {e}")



def update_animal_age():
    try:
        name = input("Введіть ім'я тварини: ")
        new_age = int(input("Введіть новий вік: "))
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count:
            print("Вік оновлено успішно.")
        else:
            print("Документ не знайдено.")
    except PyMongoError as e:
        print(f"Помилка при оновленні: {e}")

def add_feature_to_animal():
    try:
        name = input("Введіть ім'я тварини: ")
        new_feature = input("Введіть нову особливість: ")
        result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
        if result.matched_count:
            print("Особливість додано.")
        else:
            print("Документ не знайдено.")
    except PyMongoError as e:
        print(f"Помилка при оновленні: {e}")

def delete_document_by_name():
    try:
        name = input("Введіть ім'я тварини для видалення: ")
        result = collection.delete_one({"name": name})
        if result.deleted_count:
            print("Документ видалено.")
        else:
            print("Документ не знайдено.")
    except PyMongoError as e:
        print(f"Помилка при видаленні: {e}")

def delete_all_documents():
    try:
        confirmation = input("Ви впевнені, що хочете видалити всі документи? (так/ні): ")
        if confirmation.lower() == "так":
            collection.delete_many({})
            print("Всі документи видалено.")
        else:
            print("Операція скасована.")
    except PyMongoError as e:
        print(f"Помилка при видаленні: {e}")

new_cat = {
    "name": "murzik",
    "age": 2,
    "features": ["любить гратися", "сірий", "муркотить"]
}

collection.insert_one(new_cat)
print("Документ додано!")

read_document_by_name()
delete_all_documents()