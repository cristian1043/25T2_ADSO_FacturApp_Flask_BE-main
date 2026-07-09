from sqlalchemy.exc import SQLAlchemyError

from src.models import session
from src.models.clientes import Clientes


class ClientesController:

    @staticmethod
    def get():
        return session.query(Clientes).all()


    @staticmethod
    def get_by_id(id):
        return session.query(Clientes).filter_by(id=id).first()


    @staticmethod
    def save(cliente):

        try:
            session.add(cliente)
            session.commit()
            return cliente

        except SQLAlchemyError:
            session.rollback()
            return None


    @staticmethod
    def update(cliente):

        if cliente is None:
            return False

        try:
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False


    @staticmethod
    def delete(cliente):

        if cliente is None:
            return False

        try:
            session.delete(cliente)
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False