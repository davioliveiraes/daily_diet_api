from flask import Blueprint, request
from src.controllers.users_controller import UsersController
from src.models.settings.db_connection_handler import db_connection_handler
from src.utils.http_response import HttpResponse

users_bp = Blueprint('users', __name__, url_prefix='/users')

def get_users_controller():
   """Factory para criar instancias do controller"""
   db_connection_handler.connect()
   conn = db_connection_handler.get_connection()
   return UsersController(conn)

@users_bp.route('', methods=['POST'])
def create_user():
   """
   POST {{baseUrl}}/users

   Body: 
   {
      "name": "Harvey Specter",
      "email": "harvey@gmail.com"
   }
   """

   try:
      data = request.get_json()

      if not data:
         return HttpResponse.bad_request(["Dados nao fornecidos"])
      
      controller = get_users_controller()
      success, result = controller.create_user(data)

      if success:
         user_data = {
            "id": result[0],
            "name": result[1],
            "email": result[2],
            "created_at": result[3]
         }
         return HttpResponse.created(user_data, "Usuario criado com sucesso")
      else:
         return HttpResponse.bad_request(result)

   except Exception as e:
      return HttpResponse.internal_error(f"Erro interno: {str(e)}")

@users_bp.route('/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
   """
   GET {{baseUrl}}/users/{user_id}
   """
   try:
      controller = get_users_controller()
      success, result = controller.find_user_by_id(user_id)

      if success:
         user_data =  {
            "id": result[0],
            "name": result[1],
            "email": result[2],
            "created_at": result[3]
         }
         return HttpResponse.success(user_data, "Usuario encontrado")
      else:
         if "nao encontrado" in str(result):
            return HttpResponse.not_found("Usuario nao encontrado")
         else:
            return HttpResponse.bad_request(result)

   except Exception as e:
      return HttpResponse.internal_error(f"Erro interno: {str(e)}")

@users_bp.route('', methods=['GET']) 
def get_all_users():
   """GET {{baseUrl}}/users"""

   try:
      
      controller = get_users_controller()
      success, result = controller.find_all_users()

      if success:
         users_data = []
         for user in result:
            users_data.append({
               "id": user[0],
               "name": user[1],
               "email": user[2],
               "created_at": user[3]
            })
         return HttpResponse.success(users_data, f"{len(users_data)} usuarios encontrados.")
      else:
         return HttpResponse.bad_request(result)

   except Exception as e:
      return HttpResponse.internal_error(f"Erro interno: {str(e)}")

@users_bp.route('/email/<email>', methods=['GET'])
def get_user_by_email(email):
   """GET {{baseUrl}}/users/email/{email}"""

   try:
      
      controller = get_users_controller()
      success, result = controller.find_user_by_email(email)

      if success:
         user_data = {
            "id": result[0],
            "name": result[1],
            "email": result[2],
            "created_at": result[3]
         }
         return HttpResponse.success(user_data, "Usuario encontrado")
      else:
         if "nao encontrado" in str(result):
            return HttpResponse.not_found("Usuario nao encontrado")
         else:
            return HttpResponse.bad_request(result)
   
   except Exception as e:
      return HttpResponse.internal_error(f"Erro interno: {str(e)}")

@users_bp.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
   """
   PUT {{baseUrl}}/users/{user_id}

   body:
   {
      "name": "Luis Litt Atuazado",
      "email": "luis@gmail.com"
   }
   """

   try:
      data = request.get_json()

      if not data:
         return HttpResponse.bad_request(["Dados nao fornecidos"])
      
      controller = get_users_controller()
      success, result = controller.update_user(user_id, data)

      if success:
         user_data = {
            "id": result[0],
            "name": result[1],
            "email": result[2],
            "created_at": result[3]
         }
         return HttpResponse.success(user_data, "Usuario atualizado com sucesso")
      else:
         if "nao encontrado" in str(result):
            return HttpResponse.not_found("Usuario nao encontrado")
         else:
            return HttpResponse.bad_request(result)
   except Exception as e:
      return HttpResponse.internal_error(f"Erro interno: {str(e)}")

@users_bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
   """
   DELETE {{baseUrl}}/users/{user_id}
   """
   try:
      controller = get_users_controller()
      success, result = controller.delete_user(user_id)

      if success:
         return HttpResponse.success("Usuario deletado com sucesso")
      else:
         if "nao encontrado" in str(result):
            return HttpResponse.not_found("Usuario nao encontrado")
         else:
            return HttpResponse.bad_request(result)

   except Exception as e:
      return HttpResponse.internal_error(f"Erro interno: {str(e)}")
   