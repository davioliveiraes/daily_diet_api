from flask import Flask
from src.main.routes.users_routes import users_bp
from src.main.routes.meals_routes import meals_bp

def register_routes(app: Flask) -> None:
   """Registrar todas as rotas da aplicacao"""

   @app.route('/', methods=['GET'])
   def health_check():
      return {
         "message": "Daily Diet API esta funcionando!",
         "status": "healthy",
         "version": "1.0.0"
      }, 200

   app.register_blueprint(users_bp)
   app.register_blueprint(meals_bp)
