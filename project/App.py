from flask import Flask
from flask import jsonify
from project.DAO.EmpleadoDao import EmpleadoDao

app = Flask(__name__)


@app.route('/')
def show():
    workers = EmpleadoDao()
    data = workers.get_workers()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
