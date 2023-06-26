from flask import jsonify, make_response, request
from flask_jwt_extended import jwt_required
from ..app import app
from ..models import Farmacia, farmaciachemma



@app.put('/atualizar_farmacia/<int:id>')
@jwt_required()
def actualizar_farmacia(id):
    farmacia = Farmacia.query.filter_by(id_farmacia=id).first()
    try:
        farmacia.telefone = request.json["telefone"]
        farmacia.nif = request.json["nif"]
        farmacia.nome = request.json["nome"]
        farmacia.descrição = request.json["descrição"]
        farmacia.província = request.json["província"]
        farmacia.município = request.json["município"]
        farmacia.rua = request.json["rua"]
        farmacia.latitude = request.json["latitude"]
        farmacia.longitude = request.json["longitude"]
        farmacia.altitude = request.json["altitude"]
        farmacia.cadastrar()
        return make_response(jsonify({
            "Response":farmaciachemma.dump(farmacia)
        }))
    except:
        return make_response(
            jsonify({
                "Response":f"Erro ao atualizar a farmacia {farmacia.nome}"
            }),
            400
        )







