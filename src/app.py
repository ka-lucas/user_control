from flask import Flask
from flask_restx import Api

from src.resource.authentication import Authentication
from src.resource.payloads.authentication import authentication_ns
from src.resource.payloads.users import users_ns


# configs
from src.resource.users import Users

app = Flask(__name__)
api = Api(app)

# namespaces
api.add_namespace(users_ns)
api.add_namespace(authentication_ns)

# routes
users_ns.add_resource(Users, '')
authentication_ns.add_resource(Authentication, '')

"""
criando uma API com o app do flask (9)
app - instancia o namespace (12)
namespaces- terao rotas adiconadas a ele, onde cada rota esta em uma classe(15)

"""