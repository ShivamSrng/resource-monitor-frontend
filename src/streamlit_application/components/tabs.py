import streamlit as st


class Tabs:
  """
  The Tabs class is responsible for showing the tabs.
  """
  
  
  def __init__(self):
    pass


  def get_tabs(self) -> list[str]:
    """
    The function returns the tabs.
    
    Returns:
    - list[str]: The list of tabs.
    """
    
    return st.tabs(["CPU Monitorinng", "Disk Monitoring", "Memory Monitoring", "Network Monitoring", "Swapped Memory Monitoring", "Process Monitoring"])