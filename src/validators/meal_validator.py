from typing import Dict
from datetime import datetime

class MealValidator:
   def __init__(self) -> None:
      pass

   def validate_meal_creation(self, meal_infos: Dict) -> Dict:
      errors = []

      # validar_nome
      if not meal_infos.get("name"):
         errors.append("Nome da refeicao e obrigatoria.")
      elif len(meal_infos["name"].strip()) < 2:
         errors.append("Nome da refeicao deve ter pelo menos 2 caracteres.")
      elif len(meal_infos["name"].strip()) > 100:
         errors.append("Nome da refeicao deve ter no maximo 100 caracteres.")

      # validar_descricao
      if not meal_infos.get("description"):
         errors.append("Descricao da refeicao e obrigatoria.")
      elif len(meal_infos["description"].strip()) < 5:
         errors.append("Descricao deve ter pelo menos 5 caracteres.")
      elif len(meal_infos["description"].strip()) > 500:
         errors.append("Descricao deve ter no maximo 500 caracteres.")

      # validar_data_hora
      if not meal_infos.get("datetime"):
         errors.append("Data e hora da refeicao sao obrigatoria.")
      elif not self.__is_valid_datetime(meal_infos["datetime"]):
         errors.append("Data e hora devem estar no formato YYYY-MM-DD HH:MM:SS")
      
      # validar is_on_diet
      if "is_on_diet" not in meal_infos:
         errors.append("Informacao sobre dieta e obrigatoria.")
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
            errors.append("Nome da refeicao nao pode ser vazio.")
         elif len(meal_infos["name"].strip()) < 2:
            errors.append("Nome da refeicao deve ter pelo menos 2 caracteres.")
         elif len(meal_infos["name"].strip()) > 100:
            errors.append("Nome da refeicap deve ter no maximo 100 caracteres.")
      
      # validar descricao (se_fornecido)
      if "description" in meal_infos:
         if not meal_infos["description"]:
            errors.append("Descricao da refeicao nao pode ser vazia.")
         elif len(meal_infos["description"].strip()) < 5:
            errors.append("Descricao deve ter pelo menos 5 caracteres.")
         elif len(meal_infos["description"].strip()) > 500:
            errors.append("Descricao deve ter no maximo 500 caracteres.")

      # validar_data_hora (se_fornecido)
      if "datetime" in meal_infos:
         if not meal_infos["datetime"]:
            errors.append("Data e hora da refeicao nao podem ser vazias.")
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
         errors.append("ID da refeicao e obrigatorio.")
      elif not isinstance(meal_id, str):
         errors.append("ID da refeicao deve ser uma string.")
      elif len(meal_id.strip()) == 0:
         errors.append("ID da refeicao nao pode ser vazio.")
      
      return {
         "is_valid": len(errors) == 0,
         "errors": errors
      }
   
   def validate_user_id(self, user_id: str) -> Dict:
      errors = []

      if not user_id:
         errors.append("ID do usuario e obrigatorio.")
      elif not isinstance(user_id, str):
         errors.append("ID do usuario deve ser uma string.")
      elif len(user_id.strip()) == 0:
         errors.append("ID do usuario nao pode ser vazio.")
      
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

      
