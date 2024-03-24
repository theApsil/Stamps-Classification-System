import json
import re


def read_json_file(file_path: str) -> json:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка при декодировании файла '{file_path}'. Проверьте корректность формата JSON.")
        return None


def fix_data_ranges(item):
    pattern = r'([IR])\[(\d+)\s*\.\.\s*(\d+)([\])])'

    if isinstance(item, str):
        match = re.match(pattern, item)
        if match:
            prefix = match.group(1)
            start = int(match.group(2))
            stop = int(match.group(3))
            suffix = match.group(4)

            if prefix == 'I':
                return list(range(start, stop + (1 if suffix == ']' else 0)))
            elif prefix == 'R':
                return [value / 10 for value in range(start * 10, stop * 10 + (1 if suffix == ']' else 0))]

    elif isinstance(item, list):
        if len(item) == 1:
            return item[0]

    return item
