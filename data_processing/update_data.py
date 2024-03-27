from data import read_json_file, json
from classification import ABS_PATH


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
        _temp[class_name].pop(attribute)

    json_file = _temp
    with open(file_path, 'w', encoding='windows-1251') as f:
        json.dump(json_file, f, ensure_ascii=False, indent=4)


def change_attribute_value(class_name, attribute, value, json_file, file_path):
    json_file.get("Классы")[class_name][attribute] = value
    with open(file_path, 'w', encoding='windows-1251') as f:
        json.dump(json_file, f, ensure_ascii=False, indent=4)
