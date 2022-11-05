from flask_restful import Resource

from services.resources.utils import handle_request


class CustomResource(Resource):
    method_decorators = [handle_request]
