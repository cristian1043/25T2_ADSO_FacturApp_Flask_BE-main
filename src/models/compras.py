from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from src.models import Base, session
from src.models.proveedores import Proveedores
from src.models.usuarios import Usuarios


class Compras(Base):
    __tablename__ = 'compras'

    id = Column(Integer, primary_key=True)
    numero = Column(String(50), unique=True, nullable=False)
    fecha = Column(DateTime, default=datetime.now, nullable=False)
    subtotal = Column(Float, nullable=False)
    iva = Column(Float, nullable=False)
    descuento = Column(Float, nullable=False)
    total = Column(Float, nullable=False)

    id_proveedor = Column(Integer, ForeignKey('proveedores.id'), nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    def __init__(self, numero, subtotal, iva, descuento, total, id_proveedor, id_usuario):
        self.numero = numero
        self.subtotal = subtotal
        self.iva = iva
        self.descuento = descuento
        self.total = total
        self.id_proveedor = id_proveedor
        self.id_usuario = id_usuario
        
def save(self):
    session.add(self)
    session.commit()

def get():
    compras = session.query(Compras).all()
    return compras

def get_by_id(id):
    compra = session.query(Compras).filter_by(id=id).first()
    return compra

def update(self):
    session.commit()

def delete(self):
    session.delete(self)
    session.commit()