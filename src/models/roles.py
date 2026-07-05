from sqlalchemy import Column, Integer, String
from src.models import Base, session

class Roles(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(255), nullable=True)

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        
def save(self):
    session.add(self)
    session.commit()

def get():
    roles = session.query(Roles).all()
    return roles

def get_by_id(id):
    rol = session.query(Roles).filter_by(id=id).first()
    return rol

def update(self):
    session.commit()

def delete(self):
    session.delete(self)
    session.commit()