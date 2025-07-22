import pytest # type: ignore
import uuid
from datetime import datetime
from .users_repository import UsersRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
user_id = str(uuid.uuid4())
user_id_2 = str(uuid.uuid4())

unique_email = f"user_{str(uuid.uuid4())[:8]}@email.com"
unique_email_2 = f"user_{str(uuid.uuid4())[:8]}@email.com"

@pytest.mark.skip(reason="interacao com o banco")
def test_01_create_user():
    conn = db_connection_handler.get_connection()
    users_repository = UsersRepository(conn)

    user_infos = {
      "id": user_id,
      "name": "Luis Litt",
      "email": unique_email,
      "created_at": datetime.now().isoformat()
    }

    users_repository.create_user(user_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_02_second_create_user():
    conn = db_connection_handler.get_connection()
    user_repository = UsersRepository(conn)

    user_infos = {
        "id": user_id_2,
        "name": "Mike Ross",
        "email": unique_email_2,
        "created_at": datetime.now().isoformat()
    }

    user_repository.create_user(user_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_03_find_user_by_id():
    conn = db_connection_handler.get_connection()
    users_repository = UsersRepository(conn)

    users = users_repository.find_user_by_id(user_id)
    print(f"User found by ID: {users}")

@pytest.mark.skip(reason="interacao com o banco")
def test_04_find_user_by_email():
   conn = db_connection_handler.get_connection()
   users_respository = UsersRepository(conn)

   users = users_respository.find_user_by_email(unique_email)
   print(f"User found by email: {users}")

@pytest.mark.skip(reason="interacao com o banco")
def test_05_find_all_users():
   conn = db_connection_handler.get_connection()
   users_repository = UsersRepository(conn)

   users = users_repository.find_all_users()
   print(f"All users: {users}")

@pytest.mark.skip(reason="interacao com o banco")
def test_06_check_email_exists():
    conn = db_connection_handler.get_connection()
    users_repository = UsersRepository(conn)

    exists = users_repository.check_emails_exists(unique_email)
    print(f"Email exists: {exists}")

    not_exists = users_repository.check_emails_exists("naoexiste@gmail.com")
    print(f"Email not exists: {not_exists}")

@pytest.mark.skip(reason="interacao com o banco")
def test_07_update_user():
    conn = db_connection_handler.get_connection()
    users_repository = UsersRepository(conn)

    updated_email = f"updated_{str(uuid.uuid4())[:8]}@email.com"

    updated_user_infos = {
        "name": "Harvey Specter",
        "email": updated_email
    }

    users_repository.update_user(user_id, updated_user_infos)
    print("User updated successfully")

@pytest.mark.skip(reason="interacao com o banco")
def test_07_delete_user():
    conn = db_connection_handler.get_connection()
    users_repository = UsersRepository(conn)

    users_repository.delete_user(user_id_2)
    print("User deleted successfully")
    