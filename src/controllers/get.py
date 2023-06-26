from flask import jsonify, make_response, request
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta as td
from ..app import app, db
from ..models import Farmacia, farmaciaschemma



@app.get('/')
def index():
    return make_response(
        jsonify({"Response":"API no ar!"}),
        200
    )

@app.get('/login')
def login():
    farmacia = Farmacia.query.filter_by(nif=request.json['nif']).first()
    if not farmacia:
        return make_response(jsonify({
            "Response":f"Impossível logar a farmacia({request.json['nif']})"
        }))
    token = create_access_token(identity=farmacia.nome,expires_delta=td(minutes=1))
    return make_response(
        jsonify({"token":token}),
        200
    )

@app.get('/farmacias')
@jwt_required()
def pegar_farmacias():
    farmacias = Farmacia.query.all()
    return make_response(
        jsonify({
            "Response":farmaciaschemma.dump(farmacias)
        })
    )


@app.before_request
def inicializar():
    db.create_all()