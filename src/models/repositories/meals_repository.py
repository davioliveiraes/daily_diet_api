from typing import Dict, List, Tuple, Optional
from sqlite3 import Connection
import uuid
from datetime import datetime

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
   

      
   


