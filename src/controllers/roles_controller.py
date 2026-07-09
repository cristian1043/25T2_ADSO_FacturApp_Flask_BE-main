from sqlalchemy.exc import SQLAlchemyError

from src.models import session
from src.models.roles import Roles


class RolesController:

    @staticmethod
    def get():
        return session.query(Roles).all()


    @staticmethod
    def get_by_id(id):
        return session.query(Roles).filter_by(id=id).first()


    @staticmethod
    def save(rol):

        try:
            session.add(rol)
            session.commit()
            return rol

        except SQLAlchemyError:
            session.rollback()
            return None


    @staticmethod
    def update(rol):

        if rol is None:
            return False

        try:
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False


    @staticmethod
    def delete(rol):

        if rol is None:
            return False

        try:
            session.delete(rol)
            session.commit()
            return True

        except SQLAlchemyError:
            session.rollback()
            return False