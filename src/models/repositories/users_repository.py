from typing import Dict, Tuple
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