from data import read_json_file, fix_data_ranges

ABS_PATH = 'D:\Study Projects\Ontology\Stamps-Classification-System'


def classify(year: int, sort: str, place: str, nominal: str, size: str, save: str, leveling: int,
        sticker: str, perforation: int, marking: str, circulation: str, water_mark: str,
        history: str, issue: str, classes_info) -> tuple:
    res_good = ''
    res_bad = ''
    for class_name, class_data in classes_info.items():
        for attribute, value in class_data.items():
            value = fix_data_ranges(value)
            if attribute == 'Год выпуска':
                if year not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}> ∉ [{value[0]};{value[-1]}]\n'
                    break
            elif attribute == 'Сорт бумаги':
                if sort not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {sort}\n'
                    break
            elif attribute == 'Место выпуска':
                if place not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {place}\n'
                    break
            elif attribute == 'Номинал':
                if isinstance(value, list):
                    if nominal not in value:
                        res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {nominal}\n'
                        break
                elif isinstance(value, str):
                    if nominal != value:
                        res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {nominal}\n'
                        break
            elif attribute == 'Размер':
                if size not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {size}\n'
                    break
            elif attribute == 'Сохранность':
                if save not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {save}\n'
                    break
            elif attribute == 'Выравнивание':
                if leveling not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}> ∉ [{value[0]};{value[-1]}]\n'
                    break
            elif attribute == 'Наклейка':
                if isinstance(value, list):
                    if sticker not in value:
                        res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {sticker}\n'
                        break
                elif isinstance(value, str):
                    if sticker != value:
                        res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {sticker}\n'
                        break
            elif attribute == 'Перфорация':
                if perforation not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}> ∉ [{value[0]};{value[-1]}]\n'
                    break
            elif attribute == 'Маркировка':
                if marking not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {marking}\n'
                    break
            elif attribute == 'Тираж':
                if circulation not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {circulation}\n'
                    break
            elif attribute == 'Водяной знак':
                if water_mark not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {water_mark}\n'
                    break
            elif attribute == 'История':
                if history not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {history}\n'
                    break
            elif attribute == 'История':
                if issue not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {issue}\n'
                    break
            else:
                res_good += f'<{class_name}> подходит по всем параметрам.\n'

    return (res_good, res_bad)

#
# file_path = ABS_PATH + '\data_knowledge.json'
# json_data = read_json_file(file_path)
# classes_info = json_data.get("Классы")
#
#
# res = classify(2000, "офсетная бумага", "Ближний восток",
#           "Да", "20x27.5", "незначительный дефект", 90.1,
#           "Да", 12, "сильно заметная", "огромный",
#           "Нет", "Нет", "отсутствует",classes_info)
# print(f'{res[0]}\n{res[1]}')
