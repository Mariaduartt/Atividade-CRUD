from src.models.autor import Autor
from src.database import db

class AutorRepository:
    @staticmethod
    def get_all():
        return Autor.query.all()

    @staticmethod
    def get_by_id(autor_id):
        return Autor.query.get(autor_id)

    @staticmethod
    def add(autor):
        db.session.add(autor)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(autor):
        db.session.delete(autor)
        db.session.commit()