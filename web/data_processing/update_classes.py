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


def add_class(class_name, values, file_path):
    with open(file_path, 'r', encoding='windows-1251') as file:
        data = json.load(file)

    with open('D:\StudyProjects\SCS\datatypes.json', 'r') as file:
        data_types = json.load(file)

    finished_data = {}
    count = 0
    for key, val in data_types.items():
        if val == 'Интервальный':
            if count != 6:
                finished_data[key] = f'I[{values[count]}]'
            else:
                finished_data[key] = f'R[{values[count]})'
        if val == 'Качественный':
            temp = values[count].split(',')
            finished_data[key] = temp
        if val == 'Логический':
            finished_data[key] = values[count]
        count += 1

    data["Классы"][class_name] = finished_data

    with open(file_path, 'w', encoding='windows-1251') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
