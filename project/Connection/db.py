import mysql.connector as connection
from flask import g, current_app


class db:

    @staticmethod
    def get_db():
        conect = connection.connect(
                host='localhost',
                database='biometrico',
                user='root',
                password='12345'
        )
        return conect

    @staticmethod
    def close_db():
        db.get_db().close()

    @staticmethod
    def init_app(app):
        app.teardown_appcontext(db.close_db)
