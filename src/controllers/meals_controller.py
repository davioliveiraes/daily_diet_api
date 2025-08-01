from datetime import datetime
import uuid
from typing import Dict, Tuple
from sqlite3 import Connection
from src.models.repositories.meals_repository import MealsRepository
from src.models.repositories.users_repository import UsersRepository
from src.validators.meal_validator import MealValidator

class MealsController:
   def __init__(self, conn: Connection) -> None:
      self.__meals_respository = MealsRepository(conn)
      self.__users_repository = UsersRepository(conn)
      self.__meal_validator = MealValidator()

   def create_meal(self, user_id: str, meal_infos: Dict) -> Tuple:
      user_validation = self.__meal_validator.validate_user_id(user_id)
      if not user_validation["is_valid"]:
         return False, user_validation["errors"]

      meal_validation = self.__meal_validator.validate_meal_creation(meal_infos)
      if not meal_validation["is_valid"]:
         return False, meal_validation["errors"]
      
      user = self.__users_repository.find_user_by_id(user_id)
      if not user:
         return False, ["Usuário não encontrado"]
      
      meal_id = str(uuid.uuid4())
      user_meal_id = str(uuid.uuid4())

      meal_data = {
         "id": meal_id,
         "name": meal_infos["name"].strip(),
         "description": meal_infos["description"].strip(),
         "datetime": meal_infos["datetime"],
         "is_on_diet": meal_infos["is_on_diet"],
         "created_at": datetime.now().isoformat(),
         "updated_at": datetime.now().isoformat()
      }

      user_meal_data = {
         "id": user_meal_id,
         "user_id": user_id,
         "meal_id": meal_id
      }

      try:
         # criar_refeicao
         self.__meals_respository.create_meal(meal_data)
         
         # vincular refeicao_ao_usuario
         self.__meals_respository.create_user_meal(user_meal_data)

         # buscar_refeicao_criada
         created_meal = self.__meals_respository.find_meal_by_id(meal_id)
         return True, created_meal
      except Exception as e:
         return False, [f"Erro ao criar refeição: {str(e)}"]
   
   def find_meal_by_id(self, meal_id: str, user_id: str) -> Tuple:
      meal_validation = self.__meal_validator.validate_meal_id(meal_id)
      if not meal_validation["is_valid"]:
         return False, meal_validation["errors"]

      user_validation = self.__meal_validator.validate_user_id(user_id)
      if not user_validation["is_valid"]:
         return False, meal_validation["errors"]

      try:
         user_meals = self.__meals_respository.find_meals_by_user_id(user_id)
         meal_ids = [meal[0] for meal in user_meals]

         if meal_id not in meal_ids:
            return False, ["Refeição não encontrada ou não pertence ao usuário"]
         
         meal = self.__meals_respository.find_meal_by_id(meal_id)
         return True, meal
      except Exception as e:
         return False, [f"Erro ao buscar refeição: {str(e)}"]
   
   def find_meals_by_user_id(self, user_id: str) -> Tuple:
      validation = self.__meal_validator.validate_user_id(user_id)
      if not validation["is_valid"]:
         return False, validation["errors"]

      user = self.__users_repository.find_user_by_id(user_id)
      if not user:
         return False, ["Usuário não encontrado"]

      try:
         meals = self.__meals_respository.find_meals_on_diet_by_user_id(user_id)
         return True, meals
      except Exception as e:
         return False, [f"Erro ao buscar refeições: {str(e)}"]
      
   def find_meals_on_diet_user_id(self, user_id: str) -> Tuple:
      validation = self.__meal_validator.validate_user_id(user_id)
      if not validation["is_valid"]:
         return False, validation["errors"]
      
      user = self.__users_repository.find_user_by_id(user_id)
      if not user:
         return False, ["Usuário não encontrado"]

      try:
         meals = self.__meals_respository.find_meals_on_diet_by_user_id(user_id)
         return True, meals
      except Exception as e:
         return False, [f"Erro ao buscar refeições na dieta: {str(e)}"]
   
   def find_meals_off_diet_by_user_id(self, user_id: str) -> Tuple:
      validation = self.__meal_validator.validate_meal_id(user_id)
      if not validation["is_valid"]:
         return False, validation["errors"]
      
      user = self.__users_repository.find_user_by_id(user_id)
      if not user:
         return False, ["Usuário não encontrado"]
      
      try:
         meals = self.__meals_respository.find_meals_off_diet_by_user_id(user_id)
         return True, meals
      except Exception as e:
         return False, [f"Erro ao buscar refeições fora da dieta: {str(e)}"]
   
   def update_meal(self, meal_id: str, user_id: str, meal_infos: Dict) -> Tuple:
      meal_validation = self.__meal_validator.validate_meal_id(meal_id)
      if not meal_validation["is_valid"]:
         return False, meal_validation["errors"]
      
      user_validation = self.__meal_validator.validate_meal_id(user_id)
      if not user_validation["is_valid"]:
         return False, user_validation["errors"]
      
      data_validation = self.__meal_validator.validate_user_id(user_id)
      if not data_validation["is_valid"]:
         return False, data_validation["errors"]
      
      user_meals = self.__meals_respository.find_meals_by_user_id(user_id)
      meal_ids = [meal[0] for meal in user_meals]

      if meal_id not in meal_ids:
         return False, ["Refeição não encontrada ou não pertence ao usuário"]
      
      existing_meal = self.__meals_respository.find_meal_by_id(meal_id)
      update_data = {
         "name": meal_infos.get("name", existing_meal[1]).strip(),
         "description": meal_infos.get("description", existing_meal[2]).strip(),
         "datetime": meal_infos.get("datetime", existing_meal[3]),
         "is_on_diet": meal_infos.get("is_on_diet", existing_meal[4]),
         "updated_at": datetime.now().isoformat()
      }

      try:
         self.__meals_respository.update_meal(meal_id, update_data)
         updated_meal = self.__meals_respository.find_meal_by_id(meal_id)
         return True, updated_meal
      except Exception as e:
         return False, [f"Erro ao atualizar refeição: {str(e)}"]
   
   def delete_meal(self, meal_id: str, user_id: str) -> Tuple:
      meal_validation = self.__meal_validator.validate_meal_id(meal_id)
      if not meal_validation["is_valid"]:
         return False, meal_validation["errors"]

      user_validation = self.__meal_validator.validate_user_id(user_id)
      if not user_validation["is_valid"]:
         return False, user_validation["errors"]
      
      user_meals = self.__meals_respository.find_meals_by_user_id(user_id)
      meal_ids = [meal[0] for meal in user_meals]

      if meal_id not in meal_ids:
         return False, ["Refeição não encontrada ou não pertence a dieta"]
      
      try:
         self.__meals_respository.delete_meal(meal_id)
         return True, ["Refeição deletada com sucesso"]
      except Exception as e:
         return False, [f"Erro ao deletar refeição: {str(e)}"]
   
   def get_user_diet_statistics(self, user_id: str) -> Tuple:
      validation = self.__meal_validator.validate_user_id(user_id)
      if not validation["is_valid"]:
         return False, validation["errors"]
      
      user = self.__users_repository.find_user_by_id(user_id)
      if not user:
         return False, ["Usuário não encontrado"]

      try:
         statistics = self.__meals_respository.get_user_diet_statistics(user_id)
         return True, statistics
      except Exception as e:
         return False, [f"Erro ao buscar estatísticas: {str(e)}"]
      