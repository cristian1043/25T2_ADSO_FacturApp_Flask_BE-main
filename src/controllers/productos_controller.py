from sqlalchemy.exc import SQLAlchemyError

from src.models import session
from src.models.productos import Productos


class ProductosController:

    @staticmethod
    def get():
        return session.query(Productos).all()


    @staticmethod
    def get_by_id(id):
        return session.query(Productos).filter_by(id=id).first()


    @staticmethod
    def save(producto):

        try:
            session.add(producto)
            session.commit()
            return producto

        except SQLAlchemyError:
            session.rollback()
            return None


    @staticmethod
    def update():

        try:
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False


    @staticmethod
    def delete(producto):

        if producto is None:
            return False

        try:
            session.delete(producto)
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False