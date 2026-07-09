from sqlalchemy.exc import SQLAlchemyError

from src.models import session
from src.models.metodos_pago import MetodosPago


class MetodosPagoController:

    @staticmethod
    def get():
        return session.query(MetodosPago).all()


    @staticmethod
    def get_by_id(id):
        return session.query(MetodosPago).filter_by(id=id).first()


    @staticmethod
    def save(metodo_pago):

        try:
            session.add(metodo_pago)
            session.commit()
            return metodo_pago

        except SQLAlchemyError:
            session.rollback()
            return None


    @staticmethod
    def update(metodo_pago):

        if metodo_pago is None:
            return False

        try:
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False


    @staticmethod
    def delete(metodo_pago):

        if metodo_pago is None:
            return False

        try:
            session.delete(metodo_pago)
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False