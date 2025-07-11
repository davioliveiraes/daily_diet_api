import pytest # type: ignore
import uuid
from datetime import datetime
from .users_repository import UsersRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
user_id = str(uuid.uuid4())
user_id_2 = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_create_user():
   conn = db_connection_handler.get_connection()
   users_repository = UsersRepository(conn)

   user_infos = {
      "id": user_id,
      "name": "Harvey Specter",
      "email": "harvey@gmail.com",
      "created_at": datetime.now().isoformat()
   }

   users_repository.create_user(user_infos)
