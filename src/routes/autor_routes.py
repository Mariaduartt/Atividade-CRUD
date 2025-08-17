from flask import Blueprint, render_template, request, redirect, url_for
from src.services.autor_service import AutorService

autor_bp = Blueprint('autor', __name__, url_prefix='/autores')

@autor_bp.route('/')
def listar():
    autores = AutorService.listar_autores()
    return render_template('autores/list.html', autores=autores)

@autor_bp.route('/novo', methods=['GET', 'POST'])
def novo():
    if request.method == 'POST':
        AutorService.criar_autor(
            request.form['nome'],
            request.form['nacionalidade'],
            request.form['nascimento']
        )
        return redirect(url_for('autor.listar'))
    return render_template('autores/create.html')

@autor_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    autor = AutorService.obter_autor(id)
    if request.method == 'POST':
        AutorService.atualizar_autor(
            id,
            request.form['nome'],
            request.form['nacionalidade'],
            request.form['nascimento']
        )
        return redirect(url_for('autor.listar'))
    return render_template('autores/edit.html', autor=autor)

@autor_bp.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    AutorService.excluir_autor(id)
    return redirect(url_for('autor.listar'))