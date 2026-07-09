from sqlalchemy.exc import SQLAlchemyError

from src.models import session
from src.models.detalle_facturas import DetalleFacturas


class DetalleFacturasController:

    @staticmethod
    def get():
        return session.query(DetalleFacturas).all()


    @staticmethod
    def get_by_id(id):
        return session.query(DetalleFacturas).filter_by(id=id).first()


    @staticmethod
    def save(detalle_factura):

        try:
            session.add(detalle_factura)
            session.commit()
            return detalle_factura

        except SQLAlchemyError:
            session.rollback()
            return None


    @staticmethod
    def update(detalle_factura):

        if detalle_factura is None:
            return False

        try:
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False


    @staticmethod
    def delete(detalle_factura):

        if detalle_factura is None:
            return False

        try:
            session.delete(detalle_factura)
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False