import json


def add_attribute(attribute, value, json_file, file_path):
    _temp = json_file.get("Классы")
    for class_name in _temp.keys():
        _temp[class_name][attribute] = value

    json_file["Классы"] = _temp
    with open(file_path, 'w', encoding='windows-1251') as f:
        json.dump(json_file, f, ensure_ascii=False, indent=4)


def delete_attribute(attribute, json_file, file_path):
    _temp = json_file.get("Классы")
    for class_name in _temp.keys():
        if attribute in _temp.keys():
            _temp[class_name].pop(attribute)
        else:
            pass

    json_file = _temp
    with open(file_path, 'w', encoding='windows-1251') as f:
        json.dump(json_file, f, ensure_ascii=False, indent=4)


def change_attribute_value(class_name, attribute, type_attr, value, json_file, file_path):
    if type_attr == "Интервальный" and ('I' not in value or 'R' not in value):
        if value[-1] == ')':
            value = f'R[{value})'
        else:
            value = f'I[{value}]'
    if type_attr == "Качественный":
        temp = value.split(',')
        value = temp

    json_file.get("Классы")[class_name][attribute] = value
    with open(file_path, 'w', encoding='windows-1251') as f:
        json.dump(json_file, f, ensure_ascii=False, indent=4)


