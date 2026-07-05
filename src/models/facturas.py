from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from src.models import Base, session
from src.models.clientes import Clientes
from src.models.usuarios import Usuarios
from src.models.metodos_pago import MetodosPago
 

class Facturas(Base):
    __tablename__ = 'facturas'

    id = Column(Integer, primary_key=True)
    numero = Column(String(50), unique=True, nullable=False)
    fecha = Column(DateTime, default=datetime.now, nullable=False)
    subtotal = Column(Float, nullable=False)
    iva = Column(Float, nullable=False)
    descuento = Column(Float, nullable=False)
    total = Column(Float, nullable=False)

    id_cliente = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    id_metodo_pago = Column(Integer, ForeignKey('metodos_pago.id'), nullable=False)

    def __init__(self, numero, subtotal, iva, descuento, total, id_cliente, id_usuario, id_metodo_pago):
        self.numero = numero
        self.subtotal = subtotal
        self.iva = iva
        self.descuento = descuento
        self.total = total
        self.id_cliente = id_cliente
        self.id_usuario = id_usuario
        self.id_metodo_pago = id_metodo_pago
        
def save(self):
    session.add(self)
    session.commit()

def get():
    facturas = session.query(Facturas).all()
    return facturas

def get_by_id(id):
    factura = session.query(Facturas).filter_by(id=id).first()
    return factura

def update(self):
    session.commit()

def delete(self):
    session.delete(self)
    session.commit()