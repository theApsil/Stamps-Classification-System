import json


def remove_class_from_json(class_name, file_path):
    with open(file_path, 'r', encoding='windows-1251') as file:
        data = json.load(file)

    if class_name in data["Классы"]:
        del data["Классы"][class_name]

    with open(file_path, 'w', encoding='windows-1251') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def change_class_name(class_name, new_name, file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    if class_name in data["Классы"]:
        data["Классы"][new_name] = data["Классы"].pop(class_name)
        print(f'Название класса "{class_name}" успешно изменено на "{new_name}" в JSON файле.')
    else:
        print(f'Класс "{class_name}" не найден в JSON файле.')

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
