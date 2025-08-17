from src.models.livro import Livro
from src.database import db

class LivroRepository:
    @staticmethod
    def get_all():
        return Livro.query.all()

    @staticmethod
    def get_by_id(livro_id):
        return Livro.query.get(livro_id)

    @staticmethod
    def add(livro):
        db.session.add(livro)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(livro):
        db.session.delete(livro)
        db.session.commit()