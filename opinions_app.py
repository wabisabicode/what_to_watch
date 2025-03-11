from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)


@app.route('/')
def index_view():
    return 'Совсем скоро тут будет случайное мнение о фильме!'


if __name__ == '__main__':
    app.run()
