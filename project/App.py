from flask import Flask
from project.Service.EmpleadoSrv import EmpleadoSrv

app = Flask(__name__)


@app.route('/')
def show():
    data = EmpleadoSrv.find_workers()
    result = [worker.to_json() for worker in data]
    return result


if __name__ == '__main__':
    app.run(debug=True)
