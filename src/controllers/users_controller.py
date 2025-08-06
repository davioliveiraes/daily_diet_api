from typing import Dict, Tuple
from sqlite3 import Connection
import uuid
from datetime import datetime
from src.models.repositories.users_repository import UsersRepository
from src.validators.user_validator import UserValidator

class UsersController:
   def __init__(self, conn: Connection) -> None:
      self.__users_repository = UsersRepository(conn)
      self.__user_validator = UserValidator()
   
   def create_user(self, user_infos: Dict) -> Tuple:
      validation = self.__user_validator.validate_user_creation(user_infos)
      if not validation["is_valid"]:
         return False, validation["errors"]

      existing_user = self.__users_repository.find_user_by_email(user_infos["email"])
      if existing_user:
         return False, ["Email ja esta em uso."]

      user_data = {
         "id": str(uuid.uuid4()),
         "name": user_infos["name"].strip(),
         "email": user_infos["email"].strip().lower(),
         "created_at": datetime.now().isoformat()
      }

      try:
         self.__users_repository.create_user(user_data)
         created_user = self.__users_repository.find_user_by_id(user_data["id"])
         return True, created_user
      except Exception as e:
         return False, [f"Erro ao criar usuario: {str(e)}"]
   
   def find_user_by_id(self, user_id: str) -> Tuple:
      validation = self.__user_validator.validate_user_id(user_id)
      if not validation["is_valid"]:
         return False, validation["errors"]

      try:
         user = self.__users_repository.find_user_by_id(user_id)
         if not user:
            return False, ["Usuario nao encontrado"]
         return True, user
      except Exception as e:
         return False, [f"Erro ao buscar usuario: {str(e)}"]
   
   def find_user_by_email(self, email: str) -> Tuple:
      if not email or not email.strip():
         return False, ["Email e obrigatorio."]
      
      try:
         user = self.__users_repository.find_user_by_email(email.strip().lower())
         if not user:
            return False, ["Usuario nao encontrando"]
         return True, user
      except Exception as e:
         return False, [f"Erro ao buscar usuario: {str(e)}"]
   
   def find_all_users(self) -> Tuple:
      try:
         users = self.__users_repository.find_all_users()
         return True, users
      except Exception as e:
         return False, [f"Erro ao listar usuarios: {str(e)}"]
   
   def update_user(self, user_id: str, user_infos: Dict) -> Tuple:
      id_validation = self.__user_validator.validate_user_id(user_id)
      if not id_validation["is_valid"]:
         return False, id_validation["errors"]

      data_validation = self.__user_validator.validate_user_update(user_infos)
      if not data_validation["is_valid"]:
         return False, data_validation["errors"]
      
      existing_user = self.__users_repository.find_user_by_id(user_id)
      if not existing_user:
         return False, ["Usuario nao encontrado"]

      if "email" in user_infos:
         email_user = self.__users_repository.find_user_by_email(user_infos["email"])
         if email_user and email_user[0] != user_id:
            return False, ["Email ja esta em uso."]

      update_data = {}
      if "name" in user_infos:
         update_data["name"] = user_infos["name"].strip()
      if "email" in user_infos:
         update_data["email"] = user_infos["email"].strip().lower()
      
      try:
         self.__users_repository.update_user(user_id, update_data)
         updated_user = self.__users_repository.find_user_by_id(user_id)
         return True, updated_user
      except Exception as e:
         return False, [f"Erro ao atualizar usuario: {str(e)}"]
   
   def delete_user(self, user_id: str) -> Tuple:
      validation = self.__user_validator.validate_user_id(user_id)
      if not validation["is_valid"]:
         return False, validation["errors"]

      existing_user = self.__users_repository.find_user_by_id(user_id)
      if not existing_user:
         return False, ["Usuario nao encontrado"]
      
      try:
         self.__users_repository.delete_user(user_id)
         return True, ["Usuario deletado com sucesso"]
      except Exception as e:
         return False, [f"Erro ao deletar usuario: {str(e)}"]
