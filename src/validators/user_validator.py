from typing import Dict
import re

class UserValidator:
   def __init__(self) -> None:
      pass

   def validate_user_creation(self, user_infos: Dict) -> Dict:
      errors = []

      if not user_infos.get("name"):
         errors.append("Nome é obrigatório")
      elif len(user_infos["name"].strip()) < 2:
         errors.append("Nome deve ter pelo menos 2 caracteres.")
      elif len(user_infos["name"].strip()) > 100:
         errors.append("Nome deve ter no máximo 100 caracteres.")
      
      if not user_infos.get("email"):
         errors.append("Email é obrigatório")
      elif not self.__is_valid_email(user_infos["email"]): 
         errors.append("Email deve ter um formato válido")
      elif len(user_infos["email"]) > 255:
         errors.append("Email deve ter no máximo 255 caracteres.")
      
      return {
         "is_valid": len(errors) == 0,
         "errors": errors
      }

   # validar_nome (se_fornecido)
   def validate_user_update(self, user_infos: Dict) -> Dict:
      errors = []

      if "name" in user_infos:
         if not user_infos["name"]:
            errors.append("Nome nao pode ser vazio")
         elif len(user_infos["name"].strip()) < 2:
            errors.append("Nome deve ter pelo menos 2 caracteres.")
         elif len(user_infos["name"].strip()) > 100:
            errors.append("Nome deve ter no maximo 100 caracteres.")
      if "email" in user_infos:
         if not user_infos["email"]:
            errors.append("Email nao pode ser vazio")
         elif not self.__is_valid_email(user_infos["email"]): 
            errors.append("Email deve ser ter um formato valido.")
         elif len(user_infos["email"]) > 255:
            errors.append("Email deve ter no maximo 255 caracteres.")
      
      return {
         "is_valid": len(errors) == 0,
         "errors": errors
      }

   def validate_user_id(self, user_id: str) -> Dict:
      errors = []

      if not user_id:
         errors.append("ID do usuario e obrigatorio")
      elif not isinstance(user_id, str):
         errors.append("ID do usuario deve ser uma string.")
      elif len(user_id.strip()) == 0:
         errors.append("ID do usuario nao pode ser vazio.")
      
      return {
         "is_valid": len(errors) == 0,
         "errors": errors
      }

   def __is_valid_email(self, email: str) -> bool:
      email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
      return re.match(email_pattern, email.strip()) is not None
