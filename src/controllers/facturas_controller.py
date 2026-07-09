from sqlalchemy.exc import SQLAlchemyError

from src.models import session
from src.models.facturas import Facturas


class FacturasController:

    @staticmethod
    def get():
        return session.query(Facturas).all()


    @staticmethod
    def get_by_id(id):
        return session.query(Facturas).filter_by(id=id).first()


    @staticmethod
    def save(factura):

        try:
            session.add(factura)
            session.commit()
            return factura

        except SQLAlchemyError:
            session.rollback()
            return None


    @staticmethod
    def update(factura):

        if factura is None:
            return False

        try:
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False


    @staticmethod
    def delete(factura):

        if factura is None:
            return False

        try:
            session.delete(factura)
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False