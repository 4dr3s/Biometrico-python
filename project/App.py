from flask import Flask, request
from project.Service.EmpleadoSrv import EmpleadoSrv
from project.Connection.db import init_app, get_session
from project.Config import Config

app = Flask(__name__)
app.config.from_object(Config)

init_app(app)


@app.route('/')
def show():
    data = EmpleadoSrv.find_workers(get_session())
    return data


@app.route('/empleado', methods=['POST'])
def find_worker():
    parameter = request.form.get('id_empleado')
    data = EmpleadoSrv.find_worker(get_session(), parameter)
    return data


if __name__ == '__main__':
    app.run(debug=True)
