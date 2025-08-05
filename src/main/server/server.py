from flask import Flask
from src.main.routes.app_routes import register_routes

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False

register_routes(app)

