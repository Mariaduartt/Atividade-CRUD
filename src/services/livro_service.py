from src.repositories.livro_repository import LivroRepository
from src.models.livro import Livro

class LivroService:
    @staticmethod
    def listar_livros():
        return LivroRepository.get_all()

    @staticmethod
    def criar_livro(titulo, genero, ano, autor_id):
        livro = Livro(titulo=titulo, genero=genero, ano=ano, autor_id=autor_id)
        LivroRepository.add(livro)

    @staticmethod
    def obter_livro(livro_id):
        return LivroRepository.get_by_id(livro_id)

    @staticmethod
    def atualizar_livro(livro_id, titulo, genero, ano, autor_id):
        livro = LivroRepository.get_by_id(livro_id)
        livro.titulo = titulo
        livro.genero = genero
        livro.ano = ano
        livro.autor_id = autor_id
        LivroRepository.update()

    @staticmethod
    def excluir_livro(livro_id):
        livro = LivroRepository.get_by_id(livro_id)
        LivroRepository.delete(livro)