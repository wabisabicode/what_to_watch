from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
# Для абсолютного адреса в ОС Unix/Mac.
# sqlite:////username/dev/what_to_watch/db.sqlite3

db = SQLAlchemy(app)

class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.Text, unique=True, nullable=False)
    source = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())


@app.route('/')
def index_view():
    return 'Совсем скоро тут будет случайное мнение о фильме!'


if __name__ == '__main__':
    app.run()
