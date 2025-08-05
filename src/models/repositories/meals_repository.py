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

   def update_meal(self, meal_id: str, meal_infos: Dict):
      cursor = self.__conn.cursor()
      cursor.execute(
         '''
         UPDATE meals
         SET name = ?, description = ?, datetime = ?, is_on_diet = ?, updated_at = ?
         WHERE id = ?
         ''', (
            meal_infos["name"],
            meal_infos["description"],
            meal_infos["datetime"],
            meal_infos["is_on_diet"],
            meal_infos["updated_at"],
            meal_id
         )
      )
      self.__conn.commit()
   
   def delete_meal(self, meal_id: str) -> None:
      cursor = self.__conn.cursor()

      try:
         # remove_vinculo_user_meals_primeiro
         cursor.execute(
            '''
            DELETE FROM user_meals WHERE meal_id = ?
            ''', (meal_id, )
         )

         # remove_refeicao
         cursor.execute(
            '''
            DELETE FROM meals WHERE id = ?
            ''', (meal_id, )
         )

         self.__conn.commit()
      
      except Exception as e:
         self.__conn.rollback()
         raise e
   
   def get_user_diet_statistics(self, user_id: str) -> Dict:
      cursor = self.__conn.cursor()

      # total_de_refeicoes_do_usuario
      cursor.execute(
         '''
         SELECT COUNT(*) FROM meals m
         INNER JOIN user_meals um ON m.id = um.meal_id
         WHERE um.user_id = ?
         ''', (user_id, )
      )
      total_meals = cursor.fetchone()[0]

      # refeicoes_dentro_da_dieta
      cursor.execute(
         '''
         SELECT COUNT(*) FROM meals m
         INNER JOIN user_meals um ON m.id = um.meal_id
         WHERE um.user_id = ? AND m.is_on_diet = 1
         ''', (user_id, )
      )
      meals_on_diet = cursor.fetchone()[0]

      # refeicoes_fora_da_dieta
      cursor.execute(
         '''
         SELECT COUNT(*) FROM meals m
         INNER JOIN user_meals um ON m.id = um.meal_id
         WHERE um.user_id = ? AND m.is_on_diet = 0
         ''', (user_id, )
      )
      meals_off_diet = cursor.fetchone()[0]

      cursor.execute(
         '''
         SELECT m.is_on_diet FROM meals m
         INNER JOIN user_meals um ON m.id = um.meal_id
         WHERE um.user_id = ?
         ORDER BY m.datetime
         ''', (user_id, )
      )

      diet_sequence = [row[0] for row in cursor.fetchall()]
      best_sequence = self.__calculate_best_diet_sequence(diet_sequence)

      return {
         "total_meals": total_meals,
         "meals_on_diet": meals_on_diet,
         "meals_off_diet": meals_off_diet,
         "best_sequence": best_sequence,
         "diet_percentage": round((meals_on_diet / total_meals * 100), 2) if total_meals > 0 else 0
      }
   
   def __calculate_best_diet_sequence(self, diet_sequence: list) -> int:
      if not diet_sequence:
         return 0
      
      max_sequence = 0
      current_sequence = 0

      for is_on_diet in diet_sequence:
         if is_on_diet == 1:
            current_sequence += 1
            max_sequence = max(max_sequence, current_sequence)
         else:
            current_sequence = 0

      return max_sequence
