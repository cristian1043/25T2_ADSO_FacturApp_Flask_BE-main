from sqlalchemy import Column, Integer, String, ForeignKey
from src.models import Base, session
from src.models.roles import Roles

class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    documento = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)
    telefono = Column(String(20), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    id_rol = Column(Integer, ForeignKey('roles.id'), nullable=False)

    def __init__(self, documento, nombre, apellido, telefono, email, username, password, id_rol):
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.username = username
        self.password = password
        self.id_rol = id_rol
        
def save(self):
    session.add(self)
    session.commit()

def get():
    usuarios = session.query(Usuarios).all()
    return usuarios

def get_by_id(id):
    usuario = session.query(Usuarios).filter_by(id=id).first()
    return usuario

def update(self):
    session.commit()

def delete(self):
    session.delete(self)
    session.commit()