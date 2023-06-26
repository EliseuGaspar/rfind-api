from flask import jsonify, make_response, request
from flask_jwt_extended import jwt_required
from ..app import app
from ..models import Farmacia




@app.post('/cadastrar')
@jwt_required()
def cadastrar_farmacia():
    corpo = request.json
    try:
        nova_farmacia = Farmacia(corpo["telefone"],corpo["nif"],corpo["nome"],corpo["descrição"],corpo["província"],corpo["município"],corpo["rua"],corpo["latitude"],corpo["longitude"],corpo["altitude"])
        nova_farmacia.cadastre_se()
        if nova_farmacia.confirmar_cadastro():
            return make_response(jsonify({"Response":f"Farmacia {corpo['nome']} cadastrada com sucesso!"}),200)
        return make_response(jsonify({"Response":f"Ocorreu um erro durante o cadastro da farmacia {corpo['nome']}"}),400)
    except:
        return make_response(
            jsonify({
                "Response":f"Não foi possível cadastrar a farmacia : {corpo['nome']}"
            }), 400
        )