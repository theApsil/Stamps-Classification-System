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
    return render_template("classification.html")


if __name__ == '__main__':
    app.run(debug=True)
