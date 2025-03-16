import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    # Для абсолютного адреса в ОС Unix/Mac.
    # sqlite:////username/dev/what_to_watch/db.sqlite3
    SECRET_KEY = os.getenv('SECRET_KEY')
