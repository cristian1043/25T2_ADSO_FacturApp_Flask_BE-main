from sqlalchemy.exc import SQLAlchemyError

from src.models import session
from src.models.detalle_compras import DetalleCompras


class DetalleComprasController:

    @staticmethod
    def get():
        return session.query(DetalleCompras).all()


    @staticmethod
    def get_by_id(id):
        return session.query(DetalleCompras).filter_by(id=id).first()


    @staticmethod
    def save(detalle_compra):

        try:
            session.add(detalle_compra)
            session.commit()
            return detalle_compra

        except SQLAlchemyError:
            session.rollback()
            return None


    @staticmethod
    def update(detalle_compra):

        if detalle_compra is None:
            return False

        try:
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False


    @staticmethod
    def delete(detalle_compra):

        if detalle_compra is None:
            return False

        try:
            session.delete(detalle_compra)
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False