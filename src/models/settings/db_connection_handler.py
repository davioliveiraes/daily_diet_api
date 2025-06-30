import sqlite3
from sqlite3 import Connection
from datetime import datetime

class DbConnectionHandler:
   def __init__(self) -> None:
      self.__connection_string="storage.db"
      self.__conn = None
      self.__setup_datetime_adapters()
   
   def __setup_datetime_adapters(self) -> None:
      def adapt_datetime(ts):
         return ts.isoformat()

      def convert_datetime(s):
         return datetime.fromisoformat(s.decode())
      
      sqlite3.register_adapter(datetime, adapt_datetime)
      sqlite3.register_converter("DATETIME", convert_datetime)
   
   def connect(self) -> None:
      conn = sqlite3.connect(self.__connection_string, check_same_thread=False)
      self.__conn = conn
   
   def get_connection(self) -> Connection:
      return self.__conn # type: ignore
   
db_connection_handler = DbConnectionHandler()