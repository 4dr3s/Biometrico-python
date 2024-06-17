from flask import Flask, request, jsonify
from project.Service.EmpleadoSrv import EmpleadoSrv

app = Flask(__name__)


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
