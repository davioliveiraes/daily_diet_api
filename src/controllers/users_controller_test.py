import pytest # type: ignore
import uuid
from .users_controller import UsersController
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
conn = db_connection_handler.get_connection()
users_controller = UsersController(conn)

user_id = None

@pytest.mark.skip(reason="interacao com o banco")
def test_01_create_user_valid():
   user_infos = {
      "name": "Luis Litt",
      "email": f"luis_{str(uuid.uuid4())[:8]}@gmail.com"
   }

   success, result = users_controller.create_user(user_infos)
   print(f"Create user result: success={success}, result={result}")

   global user_id
   if success:
      user_id = result[0]
   
   assert success == True

@pytest.mark.skip(reason="interacao com o banco")
def test_02_create_user_invalid_email():
   user_infos = {
      "name": "Naruto Usumaki",
      "email": "email-invalido"
   }

   success, result = users_controller.create_user(user_infos)
   print(f"Invalid email result: success={success}, result={result}")

   assert success == False
   assert "Email deve ter um formato válido" in result

@pytest.mark.skip(reason="interacao com o banco")
def test_03_create_user_missing_name():
   user_infos = {
      "email": "teste@gmail.com"
   }

   success, result = users_controller.create_user(user_infos)
   print(f"Missing name result: success={success}, result={result}")

   assert success == False
   assert "Nome é obrigatório" in result

@pytest.mark.skip(reason="interacao com o banco")
def test_04_find_user_by_id():
   if not user_id:
      print("Skipping: user_id not available")
      return
   
   success, result = users_controller.find_user_by_id(user_id)
   print(f"Find user by ID result: success={success}, result={result}")

   assert success == True
   assert result[0] == user_id

@pytest.mark.skip(reason="interacao com o banco")
def test_05_find_user_by_id_not_found():
   fake_id = str(uuid.uuid4())

   success, result = users_controller.find_user_by_id(fake_id)
   print(f"User not found result: success={success}, result={result}")

   assert success == False
   assert "Usuário não encontrado" in result

@pytest.mark.skip(reason="interacao com o banco")
def test_06_find_all_users():
   success, result = users_controller.find_all_users()
   print(f"Find all users result: success={success}, count={len(result) if success else 0}")

   assert success == True
   assert len(result) >= 1

@pytest.mark.skip(reason="interacao com o banco")
def test_07_update_user():
   # Exemplo de pegar especificamente o user_id cadastrado no banco para atualizar!
   # user_id = "a135fbd7-635d-4d54-b261-97da25fd4a4a"

   # Para executar o user_id espeficamente, tem que comentar if abaixo!
   if not user_id:
      print("Skipping: user_id not available")
      return

   update_infos = {
      "name": "Jose Harvey Specter atualizado",
      "email": f"harvey_updated_{str(uuid.uuid4())[:8]}@gmail.com"
   }

   success, result = users_controller.update_user(user_id, update_infos)
   print(f"Update user result: success={success}, result={result}")

   assert success == True
   assert result[1] == "Jose Harvey Specter atualizado"

@pytest.mark.skip(reason="interacao com o banco")
def test_08_update_user_not_found():
   fake_id = str(uuid.uuid4())
   update_infos = {
      "name": "Nome Teste"
   }

   success, result = users_controller.update_user(fake_id, update_infos)
   print(f"Update user not found result: success={success}, result={result}")

   assert success == False
   assert "Usuário não encontrado" in result

@pytest.mark.skip(reason="interacao com o banco")
def test_09_delete_user():
   # Exemplo de pegar especificamente o user_id cadastrado no banco para atualizar!
   # user_id = "a135fbd7-635d-4d54-b261-97da25fd4a4a"

   # Para executar o user_id espeficamente, tem que comentar if abaixo!
   if not user_id:
      print("Skipping: user_id not available")
      return

   success, result = users_controller.delete_user(user_id)
   print(f"Delete user result: success={success}, result={result}")

   assert success == True
   assert "Usuário deletado com sucesso" in result
