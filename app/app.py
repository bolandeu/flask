import os

from flask import Flask, render_template, request

from config import DB_NAME


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', title='Главная страница', dom=str(request.base_url))


@app.route("/catalog")
def listing():
    return render_template('listing.html', title='Список компаний')


@app.route("/catalog/<variable>")
def card(variable):
    return render_template('card.html', title='Карточка товара')


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title='Страница не найдена')


if __name__ == "__main__":
    app.run(debug=True)
