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
   