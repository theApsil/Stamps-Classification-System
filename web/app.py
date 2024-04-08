import json
import os


from flask import Flask, render_template, request



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


def generate_table_html(data_types):
    html = '<form>'
    html += '<table align="center">\n<thead>\n<tr>\n<th>Признак</th>\n<th>Тип данных</th>\n<th>Значение</th>\n</tr>\n</thead>\n<tbody>\n'
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
            # values = get_combox_values(key, '../data_knowledge.json')
            for item in range(3):
                html += '<option value="{}">{}</option>'.format(item, item)
            html += '</select></td>\n'
        html += '</tr>\n'
    html += '</tbody>\n</table>\n'
    html += '</form>'
    return html


if __name__ == '__main__':
    app.run(debug=True)