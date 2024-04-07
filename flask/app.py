from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home_page.html")

#
# @app.route('/window1')
# def window1():
#     return render_template('window1.html')
#
#
# @app.route('/window2')
# def window2():
#     return render_template('window2.html')


if __name__ == '__main__':
    app.run(debug=True)
