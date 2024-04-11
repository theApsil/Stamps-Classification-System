import json


def remove_class_from_json(class_name, file_path):
    with open(file_path, 'r', encoding='windows-1251') as file:
        data = json.load(file)

    if class_name in data["Классы"]:
        del data["Классы"][class_name]

    with open(file_path, 'w', encoding='windows-1251') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
