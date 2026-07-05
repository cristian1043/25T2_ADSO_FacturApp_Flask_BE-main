from sqlalchemy import Column, Integer, String
from src.models import Base, session

class MetodosPago(Base):
    __tablename__ = 'metodos_pago'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    descripcion = Column(String(255), nullable=True)

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

def save(self):
    session.add(self)
    session.commit()

def get():
    metodos_pago = session.query(MetodosPago).all()
    return metodos_pago

def get_by_id(id):
    metodo_pago = session.query(MetodosPago).filter_by(id=id).first()
    return metodo_pago

def update(self):
    session.commit()

def delete(self):
    session.delete(self)
    session.commit()