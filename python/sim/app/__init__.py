from flask import Flask
from .routes.main_routes import main
from app.SleepJob import SleepJob
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    Swagger(app)
    app.register_blueprint(main)
    return app