from flask import Flask, request, jsonify
from project.Service.EmpleadoSrv import EmpleadoSrv
from project.Connection.db import db

app = Flask(__name__)


@app.before_request
def before():
    request.connection = db.get_db()


@app.teardown_request
def teardown(exception=None):
    db.close_connect()


@app.route('/')
def show():
    data = EmpleadoSrv.find_workers()
    result = [worker.to_json() for worker in data]
    return result


@app.route('/empleado', methods=['POST'])
def find_worker():
    parameter = request.form.get('id_empleado')
    data = EmpleadoSrv.find_worker(parameter)
    return data.to_json()


if __name__ == '__main__':
    app.run(debug=True)
