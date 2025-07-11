import pytest # type: ignore
import uuid
from datetime import datetime
from .meals_repository import MealsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
meal_id = str(uuid.uuid4())
user_id = str(uuid.uuid4())
user_meal_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_create_meal():
   conn = db_connection_handler.get_connection()
   meals_repository = MealsRepository(conn)

   meal_infos = {
      "id": meal_id,
      "name": "Omelete",
      "description": "Ovos com queijo, presento e cheiro verde",
      "datetime": "2025-07-11",
      "is_on_diet": 1,
      "created_at": datetime.now().isoformat(),
      "updated_at": datetime.now().isoformat()
   }

   meals_repository.create_meal(meal_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_create_user_meal():
   conn = db_connection_handler.get_connection()
   meals_repositoy = MealsRepository(conn)

   user_meal_infos = {
      "id": user_meal_id,
      "user_id": user_id,
      "meal_id": meal_id
   }

   meals_repositoy.create_user_meal(user_meal_infos)