from flask import Flask
from flask_restful import Api
from models.system import System

APP = Flask(__name__)
API = Api(APP)

@APP.route("/")
def index():
    return "API for SUP Dashboard v0.1"

API.add_resource(System, '/system')

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=80, debug=True)