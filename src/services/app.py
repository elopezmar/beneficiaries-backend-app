from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


app = Flask(__name__)
api = Api(app)
jwt = JWT()
