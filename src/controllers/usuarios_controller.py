from sqlalchemy.exc import SQLAlchemyError

from src.models import session
from src.models.usuarios import Usuarios


class UsuariosController:

    @staticmethod
    def get():
        return session.query(Usuarios).all()


    @staticmethod
    def get_by_id(id):
        return session.query(Usuarios).filter_by(id=id).first()


    @staticmethod
    def save(usuario):

        try:
            session.add(usuario)
            session.commit()
            return usuario

        except SQLAlchemyError:
            session.rollback()
            return None


    @staticmethod
    def update(usuario):

        if usuario is None:
            return False

        try:
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False


    @staticmethod
    def delete(usuario):

        if usuario is None:
            return False

        try:
            session.delete(usuario)
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False