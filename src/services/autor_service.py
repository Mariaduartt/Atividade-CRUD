from src.repositories.autor_repository import AutorRepository
from src.models.autor import Autor

class AutorService:
    @staticmethod
    def listar_autores():
        return AutorRepository.get_all()

    @staticmethod
    def criar_autor(nome, nacionalidade, nascimento):
        autor = Autor(nome=nome, nacionalidade=nacionalidade, nascimento=nascimento)
        AutorRepository.add(autor)

    @staticmethod
    def obter_autor(autor_id):
        return AutorRepository.get_by_id(autor_id)

    @staticmethod
    def atualizar_autor(autor_id, nome, nacionalidade, nascimento):
        autor = AutorRepository.get_by_id(autor_id)
        autor.nome = nome
        autor.nacionalidade = nacionalidade
        autor.nascimento = nascimento
        AutorRepository.update()

    @staticmethod
    def excluir_autor(autor_id):
        autor = AutorRepository.get_by_id(autor_id)
        AutorRepository.delete(autor)