import json
import os

from flask import Flask, render_template, request, redirect
from data_processing import get_combox_values

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
    with open('../datatypes.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    table_html = generate_table_html(data)
    return render_template("classification.html", table_html=table_html)


@app.route('/classify')
def classify():
    return render_template('classify.html')


@app.route('/classify', methods=['POST'])
def classify_post():
    data_form = request.args.get('classify')
    print(data_form)
    return data_form


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
    return render_template('delete_class.html')


@app.route('/delete_class', methods=['POST'])
def delete_class_post():
    data_form = request.args.get('delete_class')
    print(data_form)
    return data_form


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
            html += '<td><input type="number" name="{}" placeholder="Введите значение" min="0" max="360" step="1"></td>\n'.format(
                key.lower().replace(' ', ''))
        elif value == 'Логический':
            html += '<td>Логический</td>\n'
            html += '<td><input type="checkbox" name="{}" value="Да"> Да</td>\n'.format(key.lower().replace(' ', ''))
        elif value == 'Качественный':
            html += '<td>Качественный</td>\n'
            html += '<td><select name="{}">'.format(key.lower().replace(' ', ''))

            values = get_combox_values(key, '../data_knowledge.json')
            if key == 'Размер марки':
                print(values)
            for item in values:
                html += '<option value="{}">{}</option>'.format(item, item)
            html += '</select></td>\n'
        html += '</tr>\n'
    html += '</tbody>\n</table>\n'
    return html


if __name__ == '__main__':
    app.run(debug=True)
