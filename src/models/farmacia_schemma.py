from ..app import ma
from .farmacia_model import Farmacia


class FarmaciaSchemma(ma.SQLAlchemySchema):
    class Meta:
        model = Farmacia
    
    id_farmacia = ma.auto_field()
    telefone = ma.auto_field()
    nif = ma.auto_field()
    nome = ma.auto_field()
    descrição = ma.auto_field()
    província = ma.auto_field()
    município = ma.auto_field()
    rua = ma.auto_field()
    stock = ma.auto_field()
    latitude = ma.auto_field()
    longitude = ma.auto_field()
    altitude = ma.auto_field()
    cadastrada_em = ma.auto_field()


farmaciaschemma = FarmaciaSchemma(many=True)
farmaciachemma = FarmaciaSchemma()