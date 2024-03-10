import streamlit as st
from src.database.database_handler import DatabaseHandler


class LoginPage:
  def __init__(self):
    self.database_handler = DatabaseHandler()

  def run(self):
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