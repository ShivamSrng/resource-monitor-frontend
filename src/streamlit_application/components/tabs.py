import streamlit as st


class Tabs:
  def __init__(self):
    pass


  def get_tabs(self) -> list[str]:
    return st.tabs(["CPU Monitorinng", "Disk Monitoring", "Memory Monitoring", "Network Monitoring", "Swapped Memory Monitoring", "Process Monitoring"])