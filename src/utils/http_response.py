from flask import jsonify, Response
from typing import Any, Tuple, List, Union

class HttpResponse:
   @staticmethod
   def success(data: Any = None, message: str = "Sucesso") -> Tuple[Response, int]:
      """Resposta de sucesso padronizado"""
      response = {
         "success": True,
         "message": message
      }

      if data is not None:
         response["data"] = data
      
      return jsonify(response), 200

   @staticmethod
   def created(data: Any = None, message: str = "Criado com sucesso") -> Tuple[Response, int]:
      """Responta de criacao padronizada"""
      response = {
         "success": True,
         "message": message
      }

      if data is not None:
         response["data"] = data
      
      return jsonify(response), 201
   
   @staticmethod
   def bad_request(errors: Union[List[str], None] = None, message: str = 'Dados invalidos') -> Tuple[Response, int]:
      """Resposta de erro 404 padronizada"""
      response = {
         "success": False,
         "message": message
      }

      if errors:
         response["errors"] = errors
      
      return jsonify(response), 401
   
   @staticmethod
   def not_found(message: str = "Recurso nao encontrado") -> Tuple[Response, int]:
      """Resposta de erro 404 padronizada"""
      return jsonify({
         "success": False,
         "message": message
      }), 404
   
   @staticmethod
   def internal_error(message: str = "Erro interno do servidor") -> Tuple[Response, int]:
      """Resposta de erro 500 padronizada"""
      return jsonify({
         "success": False,
         "message": message
      }), 500
   
   @staticmethod
   def no_content(message: str = "Operacao realizada com sucesso") -> Tuple[Response, int]:
      """Resposta 204 padronizada"""
      return jsonify({
         "success": True,
         "message": message
      }), 204
