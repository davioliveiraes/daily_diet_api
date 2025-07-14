from typing import Dict, List, Tuple, Optional
from sqlite3 import Connection

class MealsRepository:
   def __init__(self, conn: Connection) -> None:
      self.__conn = conn

   def create_meal(self, meal_infos: Dict) -> None:
      cursor = self.__conn.cursor()
      cursor.execute(
         '''
         INSERT INTO meals
            (id, name, description, datetime, is_on_diet, created_at, updated_at)
         VALUES
            (?, ?, ?, ?, ?, ?, ?)
         ''', (
            meal_infos["id"],
            meal_infos["name"],
            meal_infos["description"],
            meal_infos["datetime"],
            meal_infos["is_on_diet"],
            meal_infos["created_at"],
            meal_infos["updated_at"]
         )
      )
      self.__conn.commit()
   
   def create_user_meal(self, user_meal_infos: Dict):
      cursor = self.__conn.cursor()
      cursor.execute(
         '''
         INSERT INTO user_meals
            (id, user_id, meal_id)
         VALUES
            (?, ?, ?)
         ''', (
            user_meal_infos["id"],
            user_meal_infos["user_id"],
            user_meal_infos["meal_id"]
         )
      )
      self.__conn.commit()
   
   def find_meal_by_id(self, meal_id: str) -> Tuple:
      cursor = self.__conn.cursor()
      cursor.execute(
         '''
         SELECT * FROM meals WHERE id = ?
         ''', (meal_id,)
      )
      meal = cursor.fetchone()
      return meal

   def find_meals_by_user_id(self, user_id: str) -> List:
      cursor = self.__conn.cursor()
      cursor.execute(
         '''
         SELECT m.* FROM meals m
         INNER JOIN user_meals um ON m.id = um.meal_id
         WHERE um.user_id = ?
         ORDER BY m.datetime DESC
         ''', (user_id,)
      )

      meals = cursor.fetchall()
      return meals

   def find_meals_on_diet_by_user_id(self, user_id: str) -> List:
      cursor = self.__conn.cursor()
      cursor.execute(
         '''
         SELECT m.* FROM meals m
         INNER JOIN user_meals um ON m.id = um.meal_id
         WHERE um.user_id = ? AND m.is_on_diet = 1
         ORDER BY m.datetime DESC
         ''', (user_id, )
      )

      meals = cursor.fetchall()
      return meals

   def find_meals_off_diet_by_user_id(self, user_id: str) -> List:
      cursor = self.__conn.cursor()
      cursor.execute(
         '''
         SELECT m.* FROM meals m
         INNER JOIN user_meals um on m.id = um.meal_id
         WHERE um.user_id = ? AND m.is_on_diet = 0
         ORDER BY m.datetime DESC
         ''', (user_id, )
      )
      
      meals = cursor.fetchall()
      return meals

   

      
   


