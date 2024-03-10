class MongoDBConstants:
  """
  This class contains the constants for the MongoDB connection.
  """


  def __init__(self) -> None:
    self.system_level_collection_info = {
      "connection_string": f"",
      "database_name": "users_sample_info",
      "collection_name": "system_level_info"
    }

    self.logs_info = {
      "collection_name": "execution_logs"
    }
  

  def get_connection_string(self) -> str:
    """
    This method returns the connection string for the MongoDB database.
    
    Returns:
    - str: The connection string for the MongoDB database.
    """
    
    return self.system_level_collection_info["connection_string"]


  def get_database_name(self) -> str:
    """
    This method returns the name of the database to connect to.
    
    Returns:
    - str: The name of the database to connect to.
    """
    return self.system_level_collection_info["database_name"]
  
  
  def get_collection_name(
      self,
      mode = "system_level_info") -> str:
    """
    This method returns the name of the collection to connect to.

    Returns:
    - str: The name of the collection to connect to.
    """
    
    if mode == "logs":
      return self.logs_info["collection_name"]
    return self.system_level_collection_info["collection_name"]