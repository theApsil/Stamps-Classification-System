from web.data_processing.data import read_json_file, fix_data_ranges

ABS_PATH = '/Stamps-Classification-System'


def classificate(year: int, sort: str, place: str, nominal: str, size: str, save: str, leveling: int,
        sticker: str, perforation: int, marking: str, circulation: str, water_mark: str,
        history: str, issue: str, classes_info) -> tuple:
    res_good = ''
    res_bad = ''
    for class_name, class_data in classes_info.items():
        for attribute, value in class_data.items():
            value = fix_data_ranges(value)
            if attribute == 'Год выпуска':
                if year not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}> ∉ [{value[0]};{value[-1]}]<br>'
                    break
            elif attribute == 'Сорт бумаги':
                if sort not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {sort}<br>'
                    break
            elif attribute == 'Место выпуска':
                if place not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {place}<br>'
                    break
            elif attribute == 'Номинал':
                if isinstance(value, list):
                    if nominal not in value:
                        res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {nominal}<br>'
                        break
                elif isinstance(value, str):
                    if nominal != value:
                        res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {nominal}<br>'
                        break
            elif attribute == 'Размер':
                if size not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {size}<br>'
                    break
            elif attribute == 'Сохранность':
                if save not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {save}<br>'
                    break
            elif attribute == 'Выравнивание':
                if leveling not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}> ∉ [{value[0]};{value[-1]}]<br>'
                    break
            elif attribute == 'Наклейка':
                if isinstance(value, list):
                    if sticker not in value:
                        res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {sticker}<br>'
                        break
                elif isinstance(value, str):
                    if sticker != value:
                        res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {sticker}<br>'
                        break
            elif attribute == 'Перфорация':
                if perforation not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}> ∉ [{value[0]};{value[-1]}]<br>'
                    break
            elif attribute == 'Маркировка':
                if marking not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {marking}<br>'
                    break
            elif attribute == 'Тираж':
                if circulation not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {circulation}<br>'
                    break
            elif attribute == 'Водяной знак':
                if water_mark not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {water_mark}<br>'
                    break
            elif attribute == 'История':
                if history not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {history}<br>'
                    break
            elif attribute == 'История':
                if issue not in value:
                    res_bad += f'<{class_name}> не подходит, так как <{attribute}>: {issue}<br>'
                    break
            else:
                res_good += f'<{class_name}> подходит по всем параметрам.<br>'

    return res_good, res_bad