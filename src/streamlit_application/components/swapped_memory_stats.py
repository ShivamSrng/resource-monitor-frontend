import pandas as pd
import streamlit as st
import altair as alt


class SwappedMemoryStats:
  def __init__(self) -> None:
    self.total_memory = 0
    self.available_memory = 0
    self.cnt = 0
    
    self.dataframe_memory_usage = pd.DataFrame()

  
  def prepare_for_showing_stats(self, swapped_memory_related_info: dict) -> None:
    self.total_memory = swapped_memory_related_info["swap_memory_total"]
    self.available_memory = swapped_memory_related_info["swap_memory_free"]
    self.available_used = swapped_memory_related_info["swap_memory_used"]
    self.memory_usage = swapped_memory_related_info["swap_memory_percent"]
    self.dataframe_memory_usage = pd.DataFrame(columns=["cnt", "swap_memory_percent"])
    self.dataframe_memory_usage.loc[len(self.dataframe_memory_usage)] = [self.cnt, swapped_memory_related_info["swap_memory_percent"]]
    self.cnt += 1
  

  def run(self, swapped_memory_stats: dict) -> None:
    placeholder_memory = st.empty()
    self.dataframe_memory_usage.loc[len(self.dataframe_memory_usage)] = [self.cnt, swapped_memory_stats["swap_memory_percent"]]
    self.cnt += 1

    with placeholder_memory.container():
      st.subheader('Swap Memory Usage')
      numerical_info, memory_percent_usage = st.columns([0.2, 0.8])
      with numerical_info:
        st.write("Swap Memory Numerical Information")
        st.write(f"Total Swap Memory: {swapped_memory_stats['swap_memory_total']}")
        st.write(f"Swap Memory Used: {swapped_memory_stats['swap_memory_used']}")
        st.write(f"Swap Memory Available: {swapped_memory_stats['swap_memory_free']}")
        st.write(f"Number of Bytes system has swapped in from disk: {swapped_memory_stats['swap_memory_sin']}")
        st.write(f"Number of Bytes system has swapped out from disk: {swapped_memory_stats['swap_memory_sout']}")

      with memory_percent_usage:
        st.write(f"Swap Memory Usage in Percentage: {swapped_memory_stats['swap_memory_percent']}%")
        st.altair_chart(
          alt.Chart(self.dataframe_memory_usage).mark_area().encode(
            y=alt.Y("swap_memory_percent", title="Swap Memory Usage Percentage", scale=alt.Scale(domain=(0, 100))),
            x=alt.X("cnt", title="Time"),
          )
        )