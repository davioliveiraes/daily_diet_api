import pytest # type: ignore
import uuid
from .meals_controller import MealsController
from .users_controller import UsersController
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
conn = db_connection_handler.get_connection()
meals_controller = MealsController(conn)
users_controller = UsersController(conn)

user_id = None
meal_id = None

@pytest.mark.skip(reason="interacao como banco")
def test_01_create_user_for_meals():
   user_infos = {
      "name": "Mike Ross",
      "email": f"mike_{str(uuid.uuid4())[:8]}@gmail.com"
   }

   success, result = users_controller.create_user(user_infos)
   print(f"Create user form meals result: success={success}, result={result}")

   global user_id
   if success:
      user_id = result[0]
   
   assert success == True

@pytest.mark.skip(reason="interacao como banco")
def test_02_create_meal_valid():
   # Exemplo de pegar especificamente o user_id cadastrado no banco para atualizar!
   # user_id = "f4e9b6f4-6107-44be-bf39-9aa1e34e50bc"

   # Para executar o user_id espeficamente, tem que comentar if abaixo!
   if not user_id:
      print("Skipping: user_id not available")
      return
   
   meal_infos = {
      "name": "Coxinha de batata doce",
      "description": "Coxinha de frango com massa de batata doce",
      "datetime": "2025-06-30 12:00:00",
      "is_on_diet": 1
   }

   success, result = meals_controller.create_meal(user_id, meal_infos)
   print(f"Create meal result: success={success}, result={result}")

   assert success == True

@pytest.mark.skip(reason="interacao como banco")
def test_03_create_meal_invalid_name():
   # Exemplo de pegar especificamente o user_id cadastrado no banco para atualizar!
   # user_id = "f4e9b6f4-6107-44be-bf39-9aa1e34e50bc"

   if not user_id:
      print("Skipping: user_id not available")
      return
   
   meal_infos = {
      "name": "A", # Nome muito curto
      "description": "Descrição válida da refeição",
      "datetime": "2025-06-30 12:00:00",
      "is_on_diet": 1
   }

   success, result = meals_controller.create_meal(user_id, meal_infos)
   print(f"Invalid meal name result: success={success}, result={result}")

   assert success == False
   assert "Nome da refeição deve ter pelo menos 2 caracteres." in result

@pytest.mark.skip(reason="interacao como banco")
def test_04_create_meal_invalid_datetime():
   # Exemplo de pegar especificamente o user_id cadastrado no banco para atualizar!
   # user_id = "f4e9b6f4-6107-44be-bf39-9aa1e34e50bc"

   if not user_id:
      print("Skipping: user_id not available")
      return
   
   meal_infos = {
      "name": "Pizza",
      "description": "Pizza de calabresa",
      "datetime": "30/06/2025 12:00", # Formato inválido
      "is_on_diet": 0
   }

   success, result = meals_controller.create_meal(user_id, meal_infos)
   print(f"Invalid datetime result success={success}, result={result}")

   assert success == False
   assert "Data e hora devem estar no formato YYYY-MM-DD HH:MM:SS" in result

@pytest.mark.skip(reason="interacao como banco")
def test_05_create_meal_user_not_found():
   fake_user_id = str(uuid.uuid4())

   meal_infos = {
      "name": "Hambúrguer",
      "description": "Hambúrguer com batata frita",
      "datetime": "2025-06-30 18:00:00",
      "is_on_diet": 0
   }

   success, result = meals_controller.create_meal(fake_user_id, meal_infos)
   print(f"User not found result: success={success}, result={result}")

   assert success == False
   assert "Usuário não encontrado" in result

@pytest.mark.skip(reason="interacao como banco")
def test_06_find_meal_by_id():
   # Exemplo de pegar especificamente o user_id cadastrado no banco para atualizar!
   # user_id = "f4e9b6f4-6107-44be-bf39-9aa1e34e50bc"
   # meal_id = "4469d8a8-da45-4c16-9f5d-bff6c071eb08"

   if not user_id or not meal_id:
      print("Skipping: user_id or meal_id not available")
      return

   success, result = meals_controller.find_meal_by_id(meal_id, user_id)
   print(f"Find meal by ID result: success={success}, result={result}")

   assert success == True
   assert result[0] == meal_id

@pytest.mark.skip(reason="interacao como banco")
def test_07_find_meal_by_id_not_found():
   # Exemplo de pegar especificamente o user_id cadastrado no banco para atualizar!
   # user_id = "f4e9b6f4-6107-44be-bf39-9aa1e34e50bc"

   if not user_id:
      print("Skipping: user_id not available")
      return
   
   fake_meal_id = str(uuid.uuid4())

   success, result = meals_controller.find_meal_by_id(fake_meal_id, user_id)
   print(f"Meal anot found result: success={success}, result={result}")

   assert success == False
   assert "Refeição não encontrada ou não pertence ao usuário" in result

@pytest.mark.skip(reason="interacao como banco")
def test_08_find_meals_by_user_id():
   # Exemplo de pegar especificamente o user_id cadastrado no banco para atualizar!
   # user_id = "f4e9b6f4-6107-44be-bf39-9aa1e34e50bc"

   if not user_id:
      print("Skipping: user_id not available")
      return
   
   success, result = meals_controller.find_meals_by_user_id(user_id)
   print(f"Find meals by user result: success={success}, result={result}")

   assert success == True
   assert len(result) >= 1

@pytest.mark.skip(reason="interacao como banco")
def test_09_find_meals_on_diet_by_user_id():
   # Exemplo de pegar especificamente o user_id cadastrado no banco para atualizar!
   # user_id = "f4e9b6f4-6107-44be-bf39-9aa1e34e50bc"

   if not user_id:
      print("Skipping: user_id is not available")
      return
   
   success, result = meals_controller.find_meals_on_diet_user_id(user_id)
   print(f"Find meals on diet result: success={success}, result={result}")

   assert success == True

@pytest.mark.skip(reason="interacao como banco")
def test_10_create_meal_off_diet():
   # Exemplo de pegar especificamente o user_id cadastrado no banco para atualizar!
   # user_id = "f4e9b6f4-6107-44be-bf39-9aa1e34e50bc"

   if not user_id:
      print("Skipping: user_id not available")
      return

   meal_infos = {
      "name": "Sushi",
      "description": "Sushi de camarão",
      "datetime": "2025-06-30 15:00:00",
      "is_on_diet": 0
   }

   success, result = meals_controller.create_meal(user_id, meal_infos)
   print(f"Create off-diet meal result: success={success}, result={result}")

   assert success == True

@pytest.mark.skip(reason="interacao como banco")
def test_11_find_meals_off_diet_by_user_id():
   # Exemplo de pegar especificamente o user_id cadastrado no banco para atualizar!
   # user_id = "f4e9b6f4-6107-44be-bf39-9aa1e34e50bc"

   if not user_id:
      print("Skipping: user_id not avaliable")
      return
   
   success, result = meals_controller.find_meals_off_diet_by_user_id(user_id)
   print(f"Find meals off diet result: success={success}, result={result}")

   assert success == True
   assert len(result) >= 1

@pytest.mark.skip(reason="interacao como banco")
def test_12_get_user_diet_statistics():
   # Exemplo de pegar especificamente o user_id cadastrado no banco para atualizar!
   # user_id = "f4e9b6f4-6107-44be-bf39-9aa1e34e50bc"

   if not user_id:
      print("Skipping: user_id not available")
      return
   
   success, result = meals_controller.get_user_diet_statistics(user_id)
   print(f"Diet statistics result: success={success}, result={result}")

   assert success == True
   assert "total_meals" in result
   assert "meals_on_diet" in result
   assert "meals_off_diet" in result
   assert "best_sequence" in result
   assert "diet_percentage" in result
   

@pytest.mark.skip(reason="interacao como banco")
def test_13_update_meal():
   # Exemplo de pegar especificamente o user_id e meal_id cadastrado no banco para atualizar!
   # user_id = "f4e9b6f4-6107-44be-bf39-9aa1e34e50bc"
   # meal_id = "bc5d7176-a9c7-4667-913a-d8c7b2301edd"

   if not user_id or not meal_id:
      print("Skipping: not user_id or meal_id available")
      return
   
   update_infos = {
      "name": "Omelete Verde",
      "description": "Ovos com espinafre e temperos naturais",
      "datetime": "2025-08-01 12:30:00",
      "is_on_diet": 1
   }

   success, result = meals_controller.update_meal(meal_id, user_id, update_infos)
   print(f"Update meal result: success={success}, result={result}")

   assert success == True
   assert result[1] == "Omelete Verde"

@pytest.mark.skip(reason="interacao como banco")
def test_14_update_meal_not_found():
   # Exemplo de pegar especificamente o user_id cadastrado no banco para atualizar!
   # user_id = "f4e9b6f4-6107-44be-bf39-9aa1e34e50bc"

   if not user_id:
      print("Skipping: user_id not available")
      return

   fake_meal_id = str(uuid.uuid4())
   update_infos = {
      "name": "Nome refeicao teste"
   }

   success, result = meals_controller.update_meal(fake_meal_id, user_id, update_infos)
   print(f"Update meal not found result: success={success}, result={result}")

   assert success == False
   assert "Refeição não encontrada ou não pertence ao usuário" in result

@pytest.mark.skip(reason="interacao como banco")
def test_15_delete_meal():
   # Exemplo de pegar especificamente o user_id e meal_id cadastrado no banco para atualizar!
   # user_id = "f4e9b6f4-6107-44be-bf39-9aa1e34e50bc"
   # meal_id = "4469d8a8-da45-4c16-9f5d-bff6c071eb08"

   if not user_id or not meal_id:
      print("Skipping: user_id or meal_id not available")
      return

   success, result = meals_controller.delete_meal(meal_id, user_id)
   print(f"Delete meal result: success={success}, result={result}")

   assert success == True
   assert "Refeição deletada com sucesso" in str(result)

@pytest.mark.skip(reason="interacao como banco")
def test_16_delete_user_cleanup():
   # Exemplo de pegar especificamente o user_id cadastrado no banco para atualizar!
   user_id = "f4e9b6f4-6107-44be-bf39-9aa1e34e50bc"

   if not user_id:
      print("Skipping: user_id not available")
      return

   success, result = users_controller.delete_user(user_id)
   print(f"Cleanup user result: success={success}, result={result}")

   assert success == True