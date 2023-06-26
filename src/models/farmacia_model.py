from ..app import db



class Farmacia(db.Model):
    __tablename__ = 'farmacias'
    id_farmacia = db.Column(db.Integer, autoincrement = True, primary_key = True, nullable = False, unique = True)
    telefone = db.Column(db.String(120), nullable = False, unique = True)
    nif = db.Column(db.String(120), nullable = False, unique = True)
    nome = db.Column(db.String(255), nullable = False)
    descrição = db.Column(db.Text, nullable = False)
    província = db.Column(db.String(120), nullable = False)
    município = db.Column(db.String(120), nullable = False)
    rua = db.Column(db.String(120), nullable = False)
    stock = db.Column(db.Integer, nullable = False)
    latitude = db.Column(db.String(120), nullable = False)
    longitude = db.Column(db.String(120), nullable = False)
    altitude = db.Column(db.String(120), nullable = False)
    cadastrada_em = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), onupdate=db.func.now())

    def __init__(self, telefone, nif, nome, descrição, província, município, rua, latitude, longitude, altitude, stock = 0):
        self.telefone = telefone
        self.nif = nif
        self.nome = nome
        self.descrição = descrição
        self.província = província
        self.município = município
        self.rua = rua
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.stock = stock
    
    def __repr__(self):
        return f'farmacia : {self.nome}'
    
    def cadastre_se(self, ):
        db.session.add(self)
        db.session.commit()
    
    def confirmar_cadastro(self, ) -> bool:
        response = self.query.filter_by(nif=self.nif)
        if response: return True
        return False
    
    def apague_se(self) -> None:
        db.session.delete(self)
        db.session.commit()