import pandas as pd
import streamlit as st
import altair as alt


class DiskStats:
  def __init__(self) -> None:
    self.total_disk = 0
    self.used_disk = 0
    self.free_disk = 0
    self.cnt = 0
    
    self.dataframe_disk_usage = pd.DataFrame()

  
  def prepare_for_showing_stats(self, disk_related_info: dict) -> None:
    self.total_disk = disk_related_info["disk_total"]
    self.used_disk = disk_related_info["disk_used"]
    self.free_disk = disk_related_info["disk_free"]
    self.disk_percent = disk_related_info["disk_percent"]
    self.dataframe_disk_usage = pd.DataFrame(columns=["cnt", "disk_percent"])
    self.dataframe_disk_usage.loc[len(self.dataframe_disk_usage)] = [self.cnt, disk_related_info["disk_percent"]]
    self.cnt += 1
  

  def run(self, disk_stats: dict) -> None:
    placeholder_disk = st.empty()
    self.dataframe_disk_usage.loc[len(self.dataframe_disk_usage)] = [self.cnt, disk_stats["disk_percent"]]
    self.cnt += 1
    with placeholder_disk.container():
      st.subheader('Disk Usage')
      numerical_info, disk_percent_usage = st.columns([0.2, 0.8])
      with numerical_info:
        st.write("Disk Numerical Information")
        st.write(f"Total Disk: {disk_stats['disk_total'] // (2**30)} GB")
        st.write(f"Used Disk: {disk_stats['disk_used'] // (2**30)} GB")
        st.write(f"Free Disk: {disk_stats['disk_free'] // (2**30)} GB")
      with disk_percent_usage:
        st.write(f"Disk Usage in Percentage: {disk_stats['disk_percent']}%")
        st.altair_chart(
          alt.Chart(self.dataframe_disk_usage).mark_area().encode(
            y=alt.Y("disk_percent", title="Disk Usage Percentage", scale=alt.Scale(domain=(0, 100))),
            x=alt.X("cnt", title="Time"),
          )
        )