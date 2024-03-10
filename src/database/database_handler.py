import consts
import pymongo
import certifi
from time import sleep


class DatabaseHandler:
  """
  The class is responsible for handling the database operations.
  """
  

  def __init__(self) -> None:
    self.mongo_client = self.__establish_connection()

    try:
      self.db = self.mongo_client[self.database_name]
      self.collection = self.db[self.collection_name]
    except Exception as err:
      print("Not able to communicate to with the website. For more information, check the logs.")
      sleep(5)
      exit(code=1)
  

  def __establish_connection(self) -> pymongo.MongoClient:
    """
    The function is responsible for establishing a connection with the MongoDB database.

    Returns:
    - pymongo.MongoClient: The MongoDB client.
    """
    self.connection_string = consts.MongoDBConstants().get_connection_string()
    self.database_name = consts.MongoDBConstants().get_database_name()
    self.collection_name = consts.MongoDBConstants().get_collection_name()

    try:
      self.mongo_client = pymongo.MongoClient(
        self.connection_string, 
        tlsCAFile=certifi.where()
      )
      client_info = self.mongo_client.server_info()
      return self.mongo_client
    
    except Exception as err:
      print("Not able to communicate to with the website. For more information, check the logs.")
      sleep(5)
      exit(code=1)
  
  
  def validate_unique_id(self, unique_id: str) -> bool:
    """
    The function is responsible for validating the unique ID.

    Args:
    - unique_id (str): The unique ID to validate.

    Returns:
    - bool: The result of the validation.
    """
    query = {"_id": unique_id}
    result = self.collection.find(query)
    return len(list(result))
  
  
  def get_resource_stats(self, unique_id: str) -> dict:
    """
    The function is responsible for getting the resource statistics.

    Args:
    - unique_id (str): The unique ID to get the resource statistics.

    Returns:
    - dict: The resource statistics.
    """
    query = {"_id": unique_id}
    result = self.collection.find(query)
    return list(result)[0]