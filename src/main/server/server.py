from flask import Flask
from src.main.routes.meals_routes import meals_routes_bp

app = Flask(__name__)

app.register_blueprint(meals_routes_bp)