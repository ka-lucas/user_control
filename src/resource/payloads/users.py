from flask_restx import Namespace, fields

# Namespaces
users_ns = Namespace('users')

# Payloads
create_payload = users_ns.model('CreatePayload', {
    'id': fields.Integer(required=True),
    'nome': fields.String(required=True),
    'senha': fields.String(required=True)
}, strict=True)

delete_payload = users_ns.model('DeletePayload', {
    'id': fields.Integer(required=True)
}, strict=True)
