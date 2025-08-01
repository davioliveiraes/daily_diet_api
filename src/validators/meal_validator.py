from typing import Dict
from datetime import datetime

class MealValidator:
   def __init__(self) -> None:
      pass

   def validate_meal_creation(self, meal_infos: Dict) -> Dict:
      errors = []

      # validar_nome
      if not meal_infos.get("name"):
         errors.append("Nome da refeição é obrigatória.")
      elif len(meal_infos["name"].strip()) < 2:
         errors.append("Nome da refeição deve ter pelo menos 2 caracteres.")
      elif len(meal_infos["name"].strip()) > 100:
         errors.append("Nome da refeição deve ter no máximo 100 caracteres.")

      # validar_descricao
      if not meal_infos.get("description"):
         errors.append("Descrição da refeição é obrigatória.")
      elif len(meal_infos["description"].strip()) < 5:
         errors.append("Descrição deve ter pelo menos 5 caracteres.")
      elif len(meal_infos["description"].strip()) > 500:
         errors.append("Descrição deve ter no máximo 500 caracteres.")

      # validar_data_hora
      if not meal_infos.get("datetime"):
         errors.append("Data e hora da refeição são obrigatória.")
      elif not self.__is_valid_datetime(meal_infos["datetime"]):
         errors.append("Data e hora devem estar no formato YYYY-MM-DD HH:MM:SS")
      
      # validar is_on_diet
      if "is_on_diet" not in meal_infos:
         errors.append("Informação sobre dieta é obrigatória.")
      elif meal_infos["is_on_diet"] not in [0, 1]:
         errors.append("Status da dieta deve ser 0 (fora da dieta) ou 1 (dentro da dieta)")
      
      return {
         "is_valid": len(errors) == 0,
         "errors": errors
      }

   def validate_meal_update(self, meal_infos: Dict) -> Dict:
      errors = []

      # validar_nome (se_fornecido)
      if "name" in meal_infos:
         if not meal_infos["name"]:
            errors.append("Nome da refeição não pode ser vazio.")
         elif len(meal_infos["name"].strip()) < 2:
            errors.append("Nome da refeição deve ter pelo menos 2 caracteres.")
         elif len(meal_infos["name"].strip()) > 100:
            errors.append("Nome da refeição deve ter no máximo 100 caracteres.")
      
      # validar descricao (se_fornecido)
      if "description" in meal_infos:
         if not meal_infos["description"]:
            errors.append("Descrição da refeição não pode ser vazia.")
         elif len(meal_infos["description"].strip()) < 5:
            errors.append("Descrição deve ter pelo menos 5 caracteres.")
         elif len(meal_infos["description"].strip()) > 500:
            errors.append("Descrição deve ter no máximo 500 caracteres.")

      # validar_data_hora (se_fornecido)
      if "datetime" in meal_infos:
         if not meal_infos["datetime"]:
            errors.append("Data e hora da refeição não podem ser vazias.")
         if not self.__is_valid_datetime(meal_infos["datetime"]): 
            errors.append("Data e hora devem estar no formato YYYY-MM-DD HH:MM:SS")

      # validar is_on_diet (se_fornecido)
      if "is_on_diet" in meal_infos:
         if meal_infos["is_on_diet"] not in [0, 1]:
            errors.append("Status da dieta deve ser 0 (fora da dieta) e 1 (dentro da dieta).")
         
      return {
         "is_valid": len(errors) == 0,
         "errors": errors
      }

   def validate_meal_id(self, meal_id: str) -> Dict:
      errors = []

      if not meal_id:
         errors.append("ID da refeição e obrigatório.")
      elif not isinstance(meal_id, str):
         errors.append("ID da refeição deve ser uma string.")
      elif len(meal_id.strip()) == 0:
         errors.append("ID da refeição não pode ser vazio.")
      
      return {
         "is_valid": len(errors) == 0,
         "errors": errors
      }
   
   def validate_user_id(self, user_id: str) -> Dict:
      errors = []

      if not user_id:
         errors.append("ID do usuário e obrigatorio.")
      elif not isinstance(user_id, str):
         errors.append("ID do usuário deve ser uma string.")
      elif len(user_id.strip()) == 0:
         errors.append("ID do usuário não pode ser vazio.")
      
      return {
         "is_valid": len(errors) == 0,
         "errors": errors
      }

   def __is_valid_datetime(self, datetime_str: str) -> bool:
      try:
         datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
         return True
      except ValueError:
         return False

      
