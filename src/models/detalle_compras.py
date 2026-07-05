from sqlalchemy import Column, Integer, Float, ForeignKey
from src.models import Base, session
from src.models.compras import Compras
from src.models.productos import Productos


class DetalleCompras(Base):
    __tablename__ = 'detalle_compras'

    id = Column(Integer, primary_key=True)
    cantidad = Column(Integer, nullable=False)
    costo_unitario = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)

    id_compra = Column(Integer, ForeignKey('compras.id'), nullable=False)
    id_producto = Column(Integer, ForeignKey('productos.id'), nullable=False)

    def __init__(self, cantidad, costo_unitario, subtotal, id_compra, id_producto):
        self.cantidad = cantidad
        self.costo_unitario = costo_unitario
        self.subtotal = subtotal
        self.id_compra = id_compra
        self.id_producto = id_producto
        
def save(self):
    session.add(self)
    session.commit()

def get():
    detalle_compras = session.query(DetalleCompras).all()
    return detalle_compras

def get_by_id(id):
    detalle_compra = session.query(DetalleCompras).filter_by(id=id).first()
    return detalle_compra

def update(self):
    session.commit()

def delete(self):
    session.delete(self)
    session.commit()