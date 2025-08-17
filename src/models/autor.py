from src.database import db

class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    nacionalidade = db.Column(db.String(50), nullable=False)
    nascimento = db.Column(db.String(10), nullable=False)
    livros = db.relationship('Livro', backref='autor', lazy=True)