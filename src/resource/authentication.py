from flask import request
from flask_restx import Resource

from src.core.authentication import AuthenticationCore
from src.resource.payloads.authentication import *

authentication_core = AuthenticationCore()


class Authentication(Resource):
    @authentication_ns.expect(log_in_payload, validate=True)
    def post(self):
        data = request.get_json()
        result = authentication_core.log_in_user(data)
        return result
