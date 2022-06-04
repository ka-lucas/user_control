from flask_restx import Namespace, fields

# Namespaces
authentication_ns = Namespace('authentication')

# Payloads
log_in_payload = authentication_ns.model('LogInPayload', {
    'id': fields.Integer(required=True),
    'nome': fields.String(required=True),
    'senha': fields.String(required=True)
}, strict=True)