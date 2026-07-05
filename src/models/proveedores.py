from sqlalchemy import Column, Integer, String
from src.models import Base, session

class Proveedores(Base):
    __tablename__ = 'proveedores'

    id = Column(Integer, primary_key=True)
    nit = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(255), nullable=False)
    contacto = Column(String(255), nullable=False)
    telefono = Column(String(20), nullable=False)
    direccion = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    def __init__(self, nit, nombre, contacto, telefono, direccion, email):
        self.nit = nit
        self.nombre = nombre
        self.contacto = contacto
        self.telefono = telefono
        self.direccion = direccion
        self.email = email
        
def save(self):
    session.add(self)
    session.commit()

def get():
    proveedores = session.query(Proveedores).all()
    return proveedores

def get_by_id(id):
    proveedor = session.query(Proveedores).filter_by(id=id).first()
    return proveedor

def update(self):
    session.commit()

def delete(self):
    session.delete(self)
    session.commit()