from flask import Blueprint, render_template, request, redirect, url_for
from src.services.livro_service import LivroService
from src.services.autor_service import AutorService

livro_bp = Blueprint('livro', __name__, url_prefix='/livros')

@livro_bp.route('/')
def listar():
    livros = LivroService.listar_livros()
    return render_template('livros/list.html', livros=livros)

@livro_bp.route('/novo', methods=['GET', 'POST'])
def novo():
    autores = AutorService.listar_autores()
    if request.method == 'POST':
        LivroService.criar_livro(
            request.form['titulo'],
            request.form['genero'],
            request.form['ano'],
            request.form['autor_id']
        )
        return redirect(url_for('livro.listar'))
    return render_template('livros/create.html', autores=autores)

@livro_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    livro = LivroService.obter_livro(id)
    autores = AutorService.listar_autores()
    if request.method == 'POST':
        LivroService.atualizar_livro(
            id,
            request.form['titulo'],
            request.form['genero'],
            request.form['ano'],
            request.form['autor_id']
        )
        return redirect(url_for('livro.listar'))
    return render_template('livros/edit.html', livro=livro, autores=autores)

@livro_bp.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    LivroService.excluir_livro(id)
    return redirect(url_for('livro.listar'))