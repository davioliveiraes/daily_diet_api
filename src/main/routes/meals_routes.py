from flask import jsonify, Blueprint, request
from src.controllers.meals_controller import MealsController
from src.models.settings.db_connection_handler import db_connection_handler
from src.utils.http_response import HttpResponse

meals_bp = Blueprint('meals', __name__, url_prefix='/meals')

def get_meals_controller():
   """Factory para criar instancia do controller"""
   db_connection_handler.connect()
   conn = db_connection_handler.get_connection()
   return MealsController(conn)


@meals_bp.route("", methods=['POST'])
def create_meal():
   """
   POST {{baseUrl}}/meals

   Body:
   {
      "user_id": "uuid-do-usuario",
      "name": "Omelete Caprese",
      "description": "Ovos com mussare de bufala, tomate e azeite",
      "datetime": "2025-08-04 12:00:00",
      "is_on_diet" 1
   }
   """
   try:
      data = request.get_json()

      if not data:
         return HttpResponse.bad_request(["Dados nao fornecidos"])
      
      user_id = data.get('user_id')
      if not user_id:
         return HttpResponse.bad_request(["user_id e obrigatorio"])
      
      meal_data = {k: v for k, v in data.items() if k != 'user_id'}

      controller = get_meals_controller()
      success, result = controller.create_meal(user_id, meal_data)

      if success:
         meal_data = {
            "id": result[0],
            "name": result[1],
            "description": result[2],
            "datetime": result[3],
            "is_on_diet": bool(result[4]),
            "created_at": result[5],
            "updated_at": result[6]
         }
         return HttpResponse.created(meal_data, "Refeicao criada com sucesso")
      else:
         return HttpResponse.bad_request(result)
   except Exception as e:
      return HttpResponse.internal_error(f"Erro interno: {str(e)}")


@meals_bp.route("/<meal_id>/user/<user_id>")
def get_meal_by_id(meal_id, user_id):
   """
   GET {{baseUrl}}/meals/{meal_id}/user/<user_id>
   """
   try:
      controller = get_meals_controller()
      success, result = controller.find_meal_by_id(meal_id, user_id)

      if success:
         meal_data = {
            "id": result[0],
            "name": result[1],
            "description": result[2],
            "datetime": result[3],
            "is_on_diet": bool(result[4]),
            "created_at": result[5],
            "update_at": result[6]
         }
         return HttpResponse.success(meal_data, "Refeicao encontrada")
      else:
         if "nao encontrada" in str(result):
            return HttpResponse.not_found("Refeicao nao encontrada")
         else:
            return HttpResponse.bad_request(result)
   except Exception as e:
      return HttpResponse.internal_error(f"Erro interno: {str(e)}")


@meals_bp.route("/user/<user_id>", methods=['GET'])
def get_meals_by_user(user_id):
   """
   GET {{baseUrl}}/meals/user/{user_id}
   """
   try:
      controller = get_meals_controller()
      success, result = controller.find_meals_by_user_id(user_id)

      if success:
         meals_data = []
         for meal in result:
            meals_data.append({
               "id": meal[0],
               "name": meal[1],
               "description": meal[2],
               "datetime": meal[3],
               "is_on_diet": bool(meal[4]),
               "created_at": meal[5],
               "updated_at": meal[6]
            })
         return HttpResponse.success(meals_data, f"{len(meals_data)} refeicoes encontradas")
      else:
         return HttpResponse.bad_request(result)
   except Exception as e:
      return HttpResponse.internal_error(f"Erro interno: {str(e)}")


@meals_bp.route("/user/<user_id>/on-diet", methods=['GET'])
def get_meals_on_diet_by_user(user_id):
   """
   GET {{baseUrl}}/meals/user/{user_id}/on-diet
   """
   try:
      controller = get_meals_controller()
      success, result = controller.find_meals_on_diet_user_id(user_id)

      if success:
         meals_data = []
         for meal in result:
            meals_data.append({
               "id": meal[0],
               "name": meal[1],
               "description": meal[2],
               "datetime": meal[3],
               "is_on_diet": bool(meal[4]),
               "created_at": meal[5],
               "updated_at": meal[6]
            })
         return HttpResponse.success(meals_data, f"{len(meals_data)} refeicoes encontradas")
      else:
         return HttpResponse.bad_request(result)

   except Exception as e:
      return HttpResponse.bad_request(result)


@meals_bp.route("/user/<user_id>/off-diet", methods=['GET'])
def get_meals_off_diet_by_user(user_id):
   """
   GET {{baseUrl}}/meals/user/{user_id}/off-diet
   """
   try:
      controller = get_meals_controller()
      success, result = controller.find_meals_off_diet_by_user_id(user_id)

      if success:
         meals_data = []
         for meal in result:
            meals_data.append({
               "id": meal[0],
               "name": meal[1],
               "description": meal[2],
               "datetime": meal[3],
               "is_on_diet": bool(meal[4]),
               "created_at": meal[5],
               "updated_at": meal[6]
            })
         return HttpResponse.success(meals_data, f"{len(meals_data)} refeicoes encontradas")
      else:
         return HttpResponse.bad_request(result)
      
   except Exception as e:
      return HttpResponse.internal_error(f"Erro interno: {str(e)}")


@meals_bp.route('/user/<user_id>/statistics', methods=['GET'])
def get_user_diet_statistics(user_id):
   """
   GET {{baseUrl}}/meals/user/{user_id}/statistics
   """
   try:
      controller = get_meals_controller()
      success, result = controller.get_user_diet_statistics(user_id)

      if success:
         return HttpResponse.success(result, "Estatisiticas da dieta obtida")
      else:
         return HttpResponse.bad_request(result)

   except Exception as e:
      return HttpResponse.internal_error(f"Erro interno: {str(e)}")


@meals_bp.route('/<meal_id>/user/<user_id>', methods=['PUT'])
def update_meal(meal_id, user_id):
   """
   PUT {{baseUrl}}/meals/{meal_id}/user/{user_id}

   Body:
   {
      "name": "Salada Verde Especial",
      "description": "Salada com molho especial",
      "datetime": "2025-06-30 12:30:00"
      "is_on_diet": 1
   }
   """
   try:
      data = request.get_json()

      if not data:
         return HttpResponse.bad_request(["Dados nao fornecidos"])
      
      controller = get_meals_controller()
      success, result = controller.update_meal(meal_id, user_id, data)

      if success:
         meal_data = {
            "id": result[0],
            "name": result[1],
            "description": result[2],
            "datetime": result[3],
            "is_on_diet": result[4],
            "created_at": result[5],
            "updated_at": result[6]
         }
         return HttpResponse.success(meal_data, "Refeicao atualizada com sucesso")
      else:
         if "nao encontrada" in str(result):
            return HttpResponse.not_found("Refeicao nao encontrada")
         else:
            return HttpResponse.bad_request(result)

   except Exception as e:
      return HttpResponse.internal_error(f"Erro interno: {str(e)}")


@meals_bp.route('/<meal_id>/user/<user_id>', methods=['DELETE'])
def delete_meal(meal_id, user_id):
   """
   DELETE {{baseUrl}}/meals/{meal_id}/user/{user_id}
   """
   try:
      controller = get_meals_controller()
      success, result = controller.delete_meal(meal_id, user_id)

      if success:
         return HttpResponse.success("Refeicao deletada com sucesso")
      else:
         if "nao encontrada" in str(result):
            return HttpResponse.not_found("Refeicao nao encontrada")
         else:
            return HttpResponse.bad_request(result)

   except Exception as e:
      return HttpResponse.internal_error(f"Erro interno: {str(e)}")