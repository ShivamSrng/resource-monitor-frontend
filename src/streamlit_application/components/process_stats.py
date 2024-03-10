import streamlit as st
import pandas as pd


class ProcessStats:
  def __init__(self) -> None:
    self.dataframe_process = pd.DataFrame()
  

  def prepare_for_showing_stats(self, process_related_info: dict) -> None:
    self.dataframe_process = pd.DataFrame(columns=["Process ID", "Image", "Session Name", "Session Num" ,"Memory Usage"])
    for process in process_related_info:
      self.dataframe_process.loc[len(self.dataframe_process)] = [process["pid"], process["image"], process["session_name"], process["session_num"], process["mem_usage"]]
  

  def run(self, process_stats: dict) -> None:
    placeholder_process = st.empty()
    for process in process_stats:
      self.dataframe_process.loc[len(self.dataframe_process)] = [process["pid"], process["image"], process["session_name"], process["session_num"], process["mem_usage"]]
    
    with placeholder_process.container():
      st.subheader('Top 10 Processes by CPU and Memory Usage')
      st.write("Process Information")
      st.dataframe(self.dataframe_process[["Process ID", "Image", "Session Name", "Session Num" ,"Memory Usage"]])