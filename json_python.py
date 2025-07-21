import json

# Данные
data = {
    "name": "Мария",
    "age": 25,
    "is_student": True
}

# Преобразуем в JSON-строку и печатаем тип
json_string = json.dumps(data, indent=4)
print(type(json_string))  # <class 'str'>

# Сохраняем в файл
with open("json_example.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# Читаем обратно из файла
with open("json_example.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
    print(loaded_data)  # {'name': 'Мария', 'age': 25, 'is_student': True}