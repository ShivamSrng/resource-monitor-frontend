import streamlit as st
from src.database.database_handler import DatabaseHandler


class LoginPage:
  """
  The LoginPage class is responsible for showing the login page.
  """
  
  
  def __init__(self) -> None:
    self.database_handler = DatabaseHandler()

  def run(self) -> tuple[str, bool]:
    """
    The function runs the login page.
    
    Returns:
    - uniqueId (str): The unique id entered by the user.
    - validate_unique_id (bool): The boolean value indicating whether the unique id is valid or not.
    """
    
    st.title('Login')
    placeholder = st.empty()
    with placeholder.container():
      uniqueId = st.text_input("Please enter your Unique ID")
      login_button = st.button('Visualize Data')
      if uniqueId and login_button:
        results_returned = self.database_handler.validate_unique_id(uniqueId)
        if results_returned:
            return uniqueId, True
        else:
            return uniqueId, False
      else:
        return uniqueId, False