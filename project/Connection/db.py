import mysql.connector as connection


class db:

    @staticmethod
    def get_db():
        connect = connection.connect(
                host='localhost',
                database='biometrico',
                user='root',
                password='12345'
        )
        return connect

    @staticmethod
    def close_connect():
        db.get_db().close()
        