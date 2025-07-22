import pytest # type: ignore
import uuid
from datetime import datetime
from .meals_repository import MealsRepository
from .users_repository import UsersRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
meal_id = str(uuid.uuid4())
user_id = str(uuid.uuid4())
user_meal_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_01_create_user():
   conn = db_connection_handler.get_connection()
   users_repository = UsersRepository(conn)

   user_infos = {
      "id": user_id,
      "name": "Rachel Zane",
      "email": f"rachel_{str(uuid.uuid4())[:8]}@email.com",
      "created_at": datetime.now().isoformat()
   }

   users_repository.create_user(user_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_02_create_meal():
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
def test_03_create_user_meal():
   conn = db_connection_handler.get_connection()
   meals_repositoy = MealsRepository(conn)

   user_meal_infos = {
      "id": user_meal_id,
      "user_id": user_id,
      "meal_id": meal_id
   }

   meals_repositoy.create_user_meal(user_meal_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_04_find_meal_by_id():
   conn = db_connection_handler.get_connection()
   meals_repository = MealsRepository(conn)

   meal = meals_repository.find_meal_by_id(meal_id)
   print(f"Meal found: {meal}")

@pytest.mark.skip(reason="interacao com o banco")
def test_05_find_meals_by_user_id():
   conn = db_connection_handler.get_connection()
   meals_repository = MealsRepository(conn)

   meals = meals_repository.find_meals_by_user_id(user_id)
   print(f"User meals: {meals}")

@pytest.mark.skip(reason="interacao com o banco")
def test_06_find_meals_on_diet_by_user_id():
   conn = db_connection_handler.get_connection()
   meals_repository = MealsRepository(conn)

   meals = meals_repository.find_meals_on_diet_by_user_id(user_id)
   print(f"Meals on diet: {meals}")

@pytest.mark.skip(reason="interacao com o banco")
def test_07_find_meals_off_diet_by_user_id():
   conn = db_connection_handler.get_connection()
   meals_repository = MealsRepository(conn)
   
   off_diet_meal_id = str(uuid.uuid4())
   off_diet_user_meal_id = str(uuid.uuid4())

   off_diet_meal_infos = {
      "id": off_diet_meal_id,
      "name": "Pizza",
      "description": "Pizze de calabresa",
      "datetime": "2025-07-15 0 19:00:00",
      "is_on_diet": 0,
      "created_at": datetime.now().isoformat(),
      "updated_at": datetime.now().isoformat()
   }

   meals_repository.create_meal(off_diet_meal_infos)

   off_diet_user_meal_infos = {
      "id": off_diet_user_meal_id,
      "user_id": user_id,
      "meal_id": off_diet_meal_id
   }

   meals_repository.create_user_meal(off_diet_user_meal_infos)

   meals = meals_repository.find_meals_off_diet_by_user_id(user_id)
   print(f"Meals off diet: {meals}")

@pytest.mark.skip(reason="interacao com o banco")
def test_08_get_user_diet_statistics():
   conn = db_connection_handler.get_connection()
   meals_repository = MealsRepository(conn)

   statistics = meals_repository.get_user_diet_statistics(user_id)
   print(f"Diet statistics: {statistics}")

@pytest.mark.skip(reason="interacao com o banco")
def test_09_update_meal():
   conn = db_connection_handler.get_connection()
   meals_repository = MealsRepository(conn)

   updated_meal_infos = {
      "name": "Omelete Especial",
      "description": "Ovo com chuchu, cebolinha verde e muçarela",
      "datetime": "2025-07-15 12:30:00",
      "is_on_diet": 1,
      "updated_at": datetime.now().isoformat()
   }

   meals_repository.update_meal(meal_id, updated_meal_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_99_delete_meal():
   conn = db_connection_handler.get_connection()
   meals_repository = MealsRepository(conn)

   meals_repository.delete_meal(meal_id)
