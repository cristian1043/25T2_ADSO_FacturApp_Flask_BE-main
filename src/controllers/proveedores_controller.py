from sqlalchemy.exc import SQLAlchemyError

from src.models import session
from src.models.proveedores import Proveedores


class ProveedoresController:

    @staticmethod
    def get():
        return session.query(Proveedores).all()


    @staticmethod
    def get_by_id(id):
        return session.query(Proveedores).filter_by(id=id).first()


    @staticmethod
    def save(proveedor):

        try:
            session.add(proveedor)
            session.commit()
            return proveedor

        except SQLAlchemyError:
            session.rollback()
            return None


    @staticmethod
    def update(proveedor):
        
        if proveedor is None:
            return False
        try:
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False


    @staticmethod
    def delete(proveedor):

        if proveedor is None:
            return False

        try:
            session.delete(proveedor)
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False