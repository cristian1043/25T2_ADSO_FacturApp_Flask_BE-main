from sqlalchemy import Column, Integer, String
from src.models import Base, session

class MetodosPago(Base):
    __tablename__ = 'metodos_pago'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    descripcion = Column(String(255), nullable=True)
 
    def save(self):
        session.add(self)
        session.commit()
        
    @staticmethod
    def get():
        return session.query(MetodosPago).all()
    
    @staticmethod
    def get_by_id(id):
        return session.query(MetodosPago).filter_by(id=id).first()
    
    def update(self):
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()
        
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion
        }