from flask import jsonify, Blueprint

meals_routes_bp = Blueprint("meal_routes", __name__)

@meals_routes_bp.route("/meals")
def hello_world():
   return "<p>HELLO WORLD, I WOULD LIKE A MEAL</p>"