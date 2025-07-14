import pytest # type: ignore
import uuid
from datetime import datetime
from .users_repository import UsersRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
user_id = str(uuid.uuid4())
user_id_2 = str(uuid.uuid4())

unique_email = f"user_{str(uuid.uuid4())[:8]}@email.com"

# @pytest.mark.skip(reason="interacao com o banco")
def test_create_user():
    conn = db_connection_handler.get_connection()
    users_repository = UsersRepository(conn)

    user_infos = {
      "id": user_id,
      "name": "Luis Litt",
      "email": unique_email,
      "created_at": datetime.now().isoformat()
   }

    users_repository.create_user(user_infos)

# @pytest.mark.skip(reason="interacao com o banco")
def test_find_user_by_id():
    conn = db_connection_handler.get_connection()
    users_repository = UsersRepository(conn)

    users = users_repository.find_user_by_id(user_id)
    print(users)

# @pytest.mark.skip(reason="interacao com o banco")
def test_find_user_by_email():
   conn = db_connection_handler.get_connection()
   users_respository = UsersRepository(conn)

   user = users_respository.find_user_by_email(unique_email)
   print(user)

# @pytest.mark.skip(reason="interacao com o banco")
def test_find_all_users():
   conn = db_connection_handler.get_connection()
   users_repository = UsersRepository(conn)

   users = users_repository.find_all_users()
   print(users)
