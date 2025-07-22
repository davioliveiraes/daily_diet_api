from typing import Dict, Tuple, List
from sqlite3 import Connection

class UsersRepository:
   def __init__(self, conn: Connection) -> None:
      self.__conn = conn
   
   def create_user(self, user_infos: Dict) -> None:
      cursor = self.__conn.cursor()
      cursor.execute(
         '''
         INSERT INTO users
            (id, name, email, created_at)
         VALUES
            (?, ?, ?, ?)
         ''', (
            user_infos["id"],
            user_infos["name"],
            user_infos["email"],
            user_infos["created_at"]
         )
      )
      self.__conn.commit()
   
   def find_user_by_id(self, user_id: str) -> Tuple:
      cursor = self.__conn.cursor()
      cursor.execute(
         '''
         SELECT * FROM users WHERE id = ?
         ''', (user_id, )
      )
      user = cursor.fetchone()
      return user

   def find_user_by_email(self, email: str) -> Tuple:
      cursor = self.__conn.cursor()
      cursor.execute(
         '''
         SELECT * FROM users WHERE email = ?
         ''', (email, )
      )
      user = cursor.fetchone()
      return user

   def find_all_users(self) -> List:
      cursor = self.__conn.cursor()
      cursor.execute(
         '''
         SELECT * FROM users ORDER BY created_at DESC
         '''
      )
      users = cursor.fetchall()
      return users
   
   def update_user(self, user_id: str, user_infos: Dict) -> None:
      cursor = self.__conn.cursor()
      cursor.execute(
         '''
         UPDATE users
         SET name = ?, email = ?
         WHERE id = ?
         ''', (
            user_infos['name'],
            user_infos['email'],
            user_id
         )
      )
      self.__conn.commit()
   
   def delete_user(self, user_id: str) -> None:
      cursor = self.__conn.cursor()

      # buscar_todas_receicoes_usuario
      cursor.execute(
         '''SELECT meal_id FROM user_meals WHERE user_id = ?''', (user_id,)
      )
      meal_ids = [row[0] for row in cursor.fetchall()]

      # remover_vinculos_user_meals
      cursor.execute(
         '''DELETE FROM meals WHERE id = ?''', (user_id, )
      )

      # remover_refeicoes_usuario
      for meal_id in meal_ids:
         cursor.execute(
            '''DELETE FROM meals WHERE id = ?''', (meal_id,)
         )
      
      # remover_usuario
      cursor.execute(
         '''DELETE FROM users WHERE id = ?''', (user_id,)
      )

      self.__conn.commit()
      
   def check_emails_exists(self, email: str) -> bool:
      cursor = self.__conn.cursor()
      cursor.execute(
         '''SELECT COUNT(*) FROM users WHERE email = ?''', (email, )
      )
      count = cursor.fetchone()[0]
      return count > 0