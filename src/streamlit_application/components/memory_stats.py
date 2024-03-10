import pandas as pd
import streamlit as st
import altair as alt


class MemoryStats:
  def __init__(self) -> None:
    self.total_memory = 0
    self.available_memory = 0
    self.cnt = 0
    
    self.dataframe_memory_usage = pd.DataFrame()

  
  def prepare_for_showing_stats(self, memory_related_info: dict) -> None:
    self.total_memory = memory_related_info["memory_total"]
    self.available_memory = memory_related_info["memory_available"]
    self.memory_usage = memory_related_info["memory_percent"]
    self.dataframe_memory_usage = pd.DataFrame(columns=["cnt", "memory_percent"])
    self.dataframe_memory_usage.loc[len(self.dataframe_memory_usage)] = [self.cnt, memory_related_info["memory_percent"]]
    self.cnt += 1
  

  def run(self, memory_stats: dict) -> None:
    placeholder_memory = st.empty()
    self.dataframe_memory_usage.loc[len(self.dataframe_memory_usage)] = [self.cnt, memory_stats["memory_percent"]]
    self.cnt += 1

    with placeholder_memory.container():
      st.subheader('Memory Usage')
      numerical_info, memory_percent_usage = st.columns([0.2, 0.8])
      with numerical_info:
        st.write("Memory Numerical Information")
        st.write(f"Total Memory: {memory_stats['memory_total'] // (2**30)} GB")
        st.write(f"Memory Available: {memory_stats['memory_available'] // (2**30)} GB")

      with memory_percent_usage:
        st.write(f"Memory Usage in Percentage: {memory_stats['memory_percent']}%")
        st.altair_chart(
          alt.Chart(self.dataframe_memory_usage).mark_area().encode(
            y=alt.Y("memory_percent", title="Memory Usage Percentage", scale=alt.Scale(domain=(0, 100))),
            x=alt.X("cnt", title="Time"),
          )
        )