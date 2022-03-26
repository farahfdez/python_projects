import flask
from flask import request, Flask, jsonify

from api_rest.ApiError import APIError
from operation.Arithmetic import Operation
from operation.ArithmeticError import Error

app = Flask(__name__)


@app.errorhandler(APIError)
def handle_exception(err):
    """Return custom JSON when APIError is raised"""
    return jsonify({"error": err.description}), err.code


@app.errorhandler(Error)
def handle_exception(err):
    """Return custom JSON when Error from operation module is raise"""
    return jsonify({"error": err.description}), err.code


def throws_api_error():
    """Throws api error if request json does not fulfill requirements"""
    raise APIError("Lists of values should be named v1 and v2", 400)


@app.route('/suma', methods=['POST'])
def sum_lists():
    try:
        v1 = request.json['v1']
        v2 = request.json['v2']
    except KeyError:
        throws_api_error()
    op = Operation(v1, v2)
    return jsonify({'result': op.sum()})


@app.route('/resta', methods=['POST'])
def subtract_lists():
    try:
        v1 = request.json['v1']
        v2 = request.json['v2']
    except KeyError:
        throws_api_error()
    op = Operation(v1, v2)
    return jsonify({'result': op.subtract()})


@app.route('/mult', methods=['POST'])
def multiply_lists():
    try:
        v1 = request.json['v1']
        v2 = request.json['v2']
    except KeyError:
        throws_api_error()
    op = Operation(v1, v2)
    return jsonify({'result': op.multiply()})


@app.route('/divis', methods=['POST'])
def divide_lists():
    try:
        v1 = request.json['v1']
        v2 = request.json['v2']
    except KeyError:
        throws_api_error()
    op = Operation(v1, v2)
    return jsonify({'result': op.divide()})


if __name__ == '__main__':
    app.run(debug=True, port=4501)
