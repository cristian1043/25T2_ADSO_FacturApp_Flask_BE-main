from sqlalchemy import Column, Integer, Float, ForeignKey
from src.models import Base, session
from src.models.facturas import Facturas
from src.models.productos import Productos


class DetalleFacturas(Base):
    __tablename__ = 'detalle_facturas'

    id = Column(Integer, primary_key=True)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)

    id_factura = Column(Integer, ForeignKey('facturas.id'), nullable=False)
    id_producto = Column(Integer, ForeignKey('productos.id'), nullable=False)

    def __init__(self, cantidad, precio_unitario, subtotal, id_factura, id_producto):
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = subtotal
        self.id_factura = id_factura
        self.id_producto = id_producto
        
def save(self):
    session.add(self)
    session.commit()

def get():
    detalle_facturas = session.query(DetalleFacturas).all()
    return detalle_facturas

def get_by_id(id):
    detalle_factura = session.query(DetalleFacturas).filter_by(id=id).first()
    return detalle_factura

def update(self):
    session.commit()

def delete(self):
    session.delete(self)
    session.commit()