from sqlalchemy.exc import SQLAlchemyError

from src.models import session
from src.models.categorias import Categorias


class CategoriasController:

    @staticmethod
    def get():
        return session.query(Categorias).all()


    @staticmethod
    def get_by_id(id):
        return session.query(Categorias).filter_by(id=id).first()


    @staticmethod
    def save(categoria):

        try:
            session.add(categoria)
            session.commit()
            return categoria

        except SQLAlchemyError:
            session.rollback()
            return None


    @staticmethod
    def update(categoria):

        if categoria is None:
            return False

        try:
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False


    @staticmethod
    def delete(categoria):

        if categoria is None:
            return False

        try:
            session.delete(categoria)
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False