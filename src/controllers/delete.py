from flask import jsonify, make_response
from flask_jwt_extended import jwt_required
from ..app import app
from ..models import Farmacia



@app.delete('/farmacia/<int:id>')
@jwt_required()
def deletar_farmacia(id):
    farmacia = Farmacia.query.filter_by(id_farmacia=id).first()
    try:
        if farmacia:
            farmacia.apague_se()
            return make_response(jsonify({
                "Response":f"{farmacia.nome} apagada com sucesso."
            }), 200)
        
        return make_response(jsonify({
            "Response":f"Não é possível deletar uma segunda vez."
        }),400)
        
    except:
        return make_response(jsonify({
            "Response":f"Ocorreu um erro ao deletar a farmacia da base."
        }),400)