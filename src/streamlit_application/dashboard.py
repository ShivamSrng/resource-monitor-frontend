from time import sleep
import streamlit as st
from src.database.database_handler import DatabaseHandler

# Components
from src.streamlit_application.components.login_page import LoginPage
from src.streamlit_application.components.tabs import Tabs
from src.streamlit_application.components.cpu_stats import CPUStats
from src.streamlit_application.components.disk_stats import DiskStats
from src.streamlit_application.components.memory_stats import MemoryStats
from src.streamlit_application.components.network_stats import NetworkStats
from src.streamlit_application.components.swapped_memory_stats import SwappedMemoryStats
from src.streamlit_application.components.process_stats import ProcessStats


class Dashboard:
  def __init__(self):
    st.set_page_config(
       layout="wide",
       page_title="Resource Monitoring Dashboard",
       page_icon="🧊"
      )
    
    self.tabs = Tabs()
    self.cpu_stats = CPUStats()
    self.disk_stats = DiskStats()
    self.memory_stats = MemoryStats()
    self.network_stats = NetworkStats()
    self.swapped_memory_stats = SwappedMemoryStats()
    self.process_stats = ProcessStats()
    self.database_handler = DatabaseHandler()
  

  def prepare_for_showing_stats(self, resource_monitor_stats: dict):
    cpu_related_info = resource_monitor_stats["cpu_info"]
    disk_related_info = resource_monitor_stats["disk_info"]
    memory_related_info = resource_monitor_stats["memory_info"]
    network_related_info = resource_monitor_stats["network_info"]
    swapped_memory_related_info = resource_monitor_stats["swap_memory_info"]
    process_related_info = resource_monitor_stats["list_of_processes"][:10]
    
    self.cpu_stats.prepare_for_showing_stats(
      cpu_related_info=cpu_related_info
    )

    self.disk_stats.prepare_for_showing_stats(
      disk_related_info=disk_related_info
    )
    
    self.memory_stats.prepare_for_showing_stats(
      memory_related_info=memory_related_info
    )
    
    self.network_stats.prepare_for_showing_stats(
      network_related_info=network_related_info
    )

    self.swapped_memory_stats.prepare_for_showing_stats(
      swapped_memory_related_info=swapped_memory_related_info
    )

    self.process_stats.prepare_for_showing_stats(
      process_related_info=process_related_info
    )
  

  def show_cpu_stats(self, cpu_related_info: dict):
    self.cpu_stats.run(cpu_stats=cpu_related_info)

  def show_disk_stats(self, disk_related_info: dict):
    self.disk_stats.run(disk_stats=disk_related_info)

  def show_memory_stats(self, memory_related_info: dict):
    self.memory_stats.run(memory_stats=memory_related_info)
  
  def show_network_stats(self, network_related_info: dict):
    self.network_stats.run(network_stats=network_related_info)

  def show_swapped_memory_stats(self, swapped_memory_related_info: dict):
    self.swapped_memory_stats.run(swapped_memory_stats=swapped_memory_related_info)

  def show_process_stats(self, process_related_info: dict):
    self.process_stats.run(process_stats=process_related_info)
  

  def run(self):
    with st.sidebar:
      unique_id, validate_unique_id = LoginPage().run()
    
    if unique_id and validate_unique_id:
      placeholder = st.empty()
      resource_monitor_stats = self.database_handler.get_resource_stats(unique_id)
      self.prepare_for_showing_stats(resource_monitor_stats)

      while True:
        with placeholder.container():
          st.title('Resource Monitoring Dashboard')
          try:
            resource_monitor_stats = self.database_handler.get_resource_stats(unique_id)
            cpu_related_info_tab, disk_related_info_tab, memory_related_info_tab, network_related_info_tab, swapped_memory_related_info_tab, process_related_info_tab = self.tabs.get_tabs()

            with cpu_related_info_tab:
              self.show_cpu_stats(
                cpu_related_info=resource_monitor_stats["cpu_info"]
              )
            
            with disk_related_info_tab:
              self.show_disk_stats(
                disk_related_info=resource_monitor_stats["disk_info"]
              )
            
            with memory_related_info_tab:
              self.show_memory_stats(
                memory_related_info=resource_monitor_stats["memory_info"]
              )
            
            with network_related_info_tab:
              self.show_network_stats(
                network_related_info=resource_monitor_stats["network_info"]
              )

            with swapped_memory_related_info_tab:
              self.show_swapped_memory_stats(
                swapped_memory_related_info=resource_monitor_stats["swap_memory_info"]
              )

            with process_related_info_tab:
              self.show_process_stats(
                process_related_info=resource_monitor_stats["list_of_processes"][:10]
              )            
          except Exception as e:
            print(e)
          finally:
            pass
          sleep(1)
    elif unique_id:
      st.write('Invalid Unique ID')

