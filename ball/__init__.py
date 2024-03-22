import os
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    
    load_dotenv()
    postgres_user = os.getenv('PG_USERNAME')
    postgres_password = os.getenv('PG_PASSWORD')
    postgres_database = os.getenv('PG_DATABASE')
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{postgres_user}:{postgres_password}@localhost:5432/{postgres_database}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    from . import models
    models.db.init_app(app)
    Migrate(app, models.db)

    @app.route('/')
    def hello():
        return 'Hello, this is PetFax!'

    from . import reptile
    app.register_blueprint(reptile.bp)
    
    return app
