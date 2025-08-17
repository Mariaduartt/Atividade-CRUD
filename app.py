import os
from flask import Flask, redirect, url_for
from src.database import db
from config import Config

def create_app():
    template_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'src', 'templates')
    app = Flask(__name__, template_folder=template_dir)
    app.config.from_object(Config)
    db.init_app(app)

    from src.models import autor, livro

    with app.app_context():
        db.create_all()

    from src.routes.autor_routes import autor_bp
    from src.routes.livro_routes import livro_bp
    app.register_blueprint(autor_bp)
    app.register_blueprint(livro_bp)

    @app.route('/')
    def index():
        return redirect(url_for('autor.listar'))

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)