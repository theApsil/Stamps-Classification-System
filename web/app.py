import json
import os

from flask import Flask, render_template, request, redirect, url_for
from data_processing import get_combox_values, remove_class_from_json, change_class_name, fix_data_ranges, classificate

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home_page.html")


@app.route('/exit')
def exit():
    os.kill(os.getpid(), 9)
    return 'Сервер остановлен'


@app.route('/classification')
def classification():
    with open('../datatypes.json', 'r') as file:
        data = json.load(file)

    table_html = generate_table_html(data)
    return render_template("classification.html", table_html=table_html)


@app.route('/classification', methods=['GET', 'POST'])
def classify_post():
    with open('../datatypes.json', 'r') as file:
        data_frame = json.load(file)

    values = []

    for key in data_frame.keys():
        temp = (key.lower()).replace(" ", "")
        values.append(request.form[temp])

    return redirect(url_for('classify', values=values))


@app.route('/classify')
def classify():
    values = request.args.getlist('values')
    temp = []
    for item in values:
        try:
            temp.append(int(item))
        except ValueError:
            temp.append(item)

    with open('../data_knowledge.json', 'r') as file:
        data = json.load(file)
    classes_info = data.get('Классы')
    year, sort, place, nominal, size, save, leveling, sticker, perforation, marking, circulation, water_mark, history, issue = temp
    res = classificate(year, sort, place, nominal, size, save, leveling, sticker, perforation, marking, circulation, water_mark, history, issue, classes_info)

    return render_template('classify.html', values=res)


@app.route('/base_editor')
def base_editor():
    return render_template('base_editor.html')


@app.route('/edit_class')
def edit_class():
    with open('../data_knowledge.json', 'r') as file:
        data = json.load(file)
    data = data.get('Классы')
    table_html = generate_class_table(data)
    return render_template('edit_class.html', table_html=table_html)


@app.route('/delete_class')
def delete_class():
    combox = generate_class_combox()
    return render_template('delete_class.html', combox=combox)


@app.route('/delete_class', methods=['GET', 'POST'])
def delete_class_post():
    del_classes = request.form['del_classes']
    remove_class_from_json(del_classes, '../data_knowledge.json')
    combox = generate_class_combox()
    return render_template('delete_class.html', combox=combox)


@app.route('/change_class')
def change_class():
    combox = generate_class_combox()
    return render_template('change_class.html', combox=combox)


@app.route('/change_class', methods=['GET', 'POST'])
def change_class_post():
    class_old = request.form['del_classes']
    class_new = request.form['new_class_name']

    change_class_name(class_old, class_new, '../data_knowledge.json')
    combox = generate_class_combox()
    return render_template('change_class.html', combox=combox)


@app.route('/attributes')
def attributes():
    combox = generate_class_combox()
    return render_template('attributes.html', combox=combox)


@app.route('/attributes', methods=['GET', 'POST'])
def attributes_table():
    _class = request.form['del_classes']
    table_html = generate_table_from_class(_class)
    return render_template('attribute_table.html', table_html=table_html)


@app.route('/change_attr_values')
def change_attr_values():
    return render_template('change_attr_values.html')


def generate_class_combox():
    with open('../data_knowledge.json', 'r') as file:
        data = json.load(file)
    data = data.get('Классы')
    html = '<select name="del_classes">\n'
    for key in data.keys():
        html += '<option value="{}">{}</option>\n'.format(key, key)
    html += '</select>\n'

    return html


def generate_table_from_class(class_name):
    with open('../data_knowledge.json', 'r') as file:
        data_class = json.load(file)
    data_class = data_class.get('Классы').get(class_name)

    with open('../datatypes.json', 'r') as f:
        data_info = json.load(f)
    html_table = "<table>\n<tr>\n<th>Признак</th>\n<th>Тип данных</th>\n<th>Значение</th>\n</tr>\n"

    for feature, data_type in data_info.items():
        for key, value in data_class.items():
            if feature == key:
                html_table += f"<tr>\n<td>{feature}</td>\n<td>{data_type}</td>\n<td>{value}</td>\n</tr>\n"

    html_table += "</table>"

    return html_table


def generate_class_table(classes):
    html = '<table align="center">\n<thead>\n<tr>\n<th> Классы </th></tr>\n</thead>\n<tbody>\n'
    for key in classes.keys():
        html += '<tr>\n<td>{}</td>\n'.format(key)
    html += '</tbody>\n</table>\n'
    return html


def generate_table_html(data_types):
    html = '<table align="center">\n<thead>\n<tr>\n<th>Признак</th>\n<th>Тип данных</th>\n<th>Значение</th>\n</tr>\n</thead>\n<tbody>\n'
    for key, value in data_types.items():
        html += '<tr>\n<td>{}</td>\n'.format(key)
        if value == 'Интервальный':
            html += '<td>Интервальный</td>\n'
            html += '<td><input type="number" name="{}" placeholder="Введите значение" min="0" max="2024" step="1"></td>\n'.format(
                key.lower().replace(' ', ''))
        elif value == 'Логический':
            html += '<td>Логический</td>\n'
            html += '<td><select name="{}">'.format(key.lower().replace(' ', ''))
            for item in ['Да', 'Нет']:
                html += '<option value="{}">{}</option>'.format(item, item)
            html += '</select></td>\n'
        elif value == 'Качественный':
            html += '<td>Качественный</td>\n'
            html += '<td><select name="{}">'.format(key.lower().replace(' ', ''))

            values = get_combox_values(key, '../data_knowledge.json')
            for item in values:
                html += '<option value="{}">{}</option>'.format(item, item)
            html += '</select></td>\n'
        html += '</tr>\n'
    html += '</tbody>\n</table>\n'
    return html


if __name__ == '__main__':
    app.run(debug=True)
