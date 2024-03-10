import pandas as pd
import streamlit as st


class CPUStats:
  """
  The CPUStats class is responsible for showing the CPU stats.
  """
  
  
  def __init__(self) -> None:
    self.total_cores = 0
    self.dataframe_cpu_percent_usage = pd.DataFrame()

  
  def prepare_for_showing_stats(self, cpu_related_info: dict) -> None:
    """
    The function prepares for showing the CPU stats.
    
    Args:
    - cpu_related_info (dict): The dictionary containing the CPU related information.
    
    Returns:
    - None
    """
    
    self.total_cores = cpu_related_info["cpu_count"]
    self.dataframe_cpu_percent_usage = pd.DataFrame(columns=[f"core_{i}" for i in range(self.total_cores)])
    

  def run(self, cpu_stats: dict) -> None:
    """
    The function runs the CPU stats.
    
    Args:
    - cpu_stats (dict): The dictionary containing the CPU stats.
    
    Returns:
    - None
    """
    
    placeholder_cpu = st.empty()
    with placeholder_cpu.container():
      st.subheader('CPU Usage')
      total_cores = cpu_stats['cpu_count']
      st.write(f"Total Cores: {total_cores}")

      k = 0
      self.dataframe_cpu_percent_usage.loc[len(self.dataframe_cpu_percent_usage)] = cpu_stats["all_cpu_percent"]
      
      for row in range(total_cores//5):
        column = st.columns(5)
        for j in range(5):
          with column[j]:
            st.write(f"Core {k+1} usage: {cpu_stats['all_cpu_percent'][k]}%")
            st.area_chart(self.dataframe_cpu_percent_usage[f"core_{k}"])
          k += 1