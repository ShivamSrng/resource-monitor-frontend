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
  """
  The Dashboard class is responsible for showing the resource monitoring stats.
  """
  
  
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
  

  def prepare_for_showing_stats(self, resource_monitor_stats: dict) -> None:
    """
    The function prepares the data for showing the stats.

    Args:
    - resource_monitor_stats (dict): The dictionary containing the resource monitor stats.

    Returns:
    - None
    """
    
    cpu_related_info = resource_monitor_stats["cpu_info"]
    disk_related_info = resource_monitor_stats["disk_info"]
    memory_related_info = resource_monitor_stats["memory_info"]
    network_related_info = resource_monitor_stats["network_info"]
    swapped_memory_related_info = resource_monitor_stats["swap_memory_info"]
    process_related_info = resource_monitor_stats["list_of_processes"][:10]
    
    # Prepare the cpu stats for showing
    self.cpu_stats.prepare_for_showing_stats(
      cpu_related_info=cpu_related_info
    )

    # Prepare the disk stats for showing
    self.disk_stats.prepare_for_showing_stats(
      disk_related_info=disk_related_info
    )
    
    # Prepare the memory stats for showing
    self.memory_stats.prepare_for_showing_stats(
      memory_related_info=memory_related_info
    )
    
    # Prepare the network stats for showing
    self.network_stats.prepare_for_showing_stats(
      network_related_info=network_related_info
    )

    # Prepare the swapped memory stats for showing
    self.swapped_memory_stats.prepare_for_showing_stats(
      swapped_memory_related_info=swapped_memory_related_info
    )

    # Prepare the process stats for showing
    self.process_stats.prepare_for_showing_stats(
      process_related_info=process_related_info
    )
  

  def show_cpu_stats(self, cpu_related_info: dict) -> None:
    """
    The function shows the CPU stats.
    
    Args:
    - cpu_related_info (dict): The dictionary containing the CPU related information.
    
    Returns:
    - None
    """
    
    self.cpu_stats.run(cpu_stats=cpu_related_info)


  def show_disk_stats(self, disk_related_info: dict) -> None:
    """
    The function shows the disk stats.
    
    Args:
    - disk_related_info (dict): The dictionary containing the disk related information.
    
    Returns:
    - None
    """
    
    self.disk_stats.run(disk_stats=disk_related_info)

  
  def show_memory_stats(self, memory_related_info: dict) -> None:
    """
    The function shows the memory stats.
    
    Args:
    - memory_related_info (dict): The dictionary containing the memory related information.
    
    Returns:
    - None
    """
    
    self.memory_stats.run(memory_stats=memory_related_info)
  
  
  def show_network_stats(self, network_related_info: dict) -> None:
    """
    The function shows the network stats.
    
    Args:
    - network_related_info (dict): The dictionary containing the network related information.
    
    Returns:
    - None
    """
    
    self.network_stats.run(network_stats=network_related_info)


  def show_swapped_memory_stats(self, swapped_memory_related_info: dict) -> None:
    """
    The function shows the swapped memory stats.
    
    Args:
    - swapped_memory_related_info (dict): The dictionary containing the swapped memory related information.
    
    Returns:
    - None
    """
    
    self.swapped_memory_stats.run(swapped_memory_stats=swapped_memory_related_info)


  def show_process_stats(self, process_related_info: dict) -> None:
    """
    The function shows the process stats.
    
    Args:
    - process_related_info (dict): The dictionary containing the process related information.
    
    Returns:
    - None
    """
    
    self.process_stats.run(process_stats=process_related_info)


  def run(self) -> None:
    """
    The function runs the dashboard.

    Returns:
    - None
    """
    
    with st.sidebar:
      # Show the login page in the sidebar
      unique_id, validate_unique_id = LoginPage().run()
    
    if unique_id and validate_unique_id:
      # Show the resource monitoring dashboard if the user has entered the unique id
      placeholder = st.empty()
      resource_monitor_stats = self.database_handler.get_resource_stats(unique_id)
      
      # Prepare the data for showing the stats
      self.prepare_for_showing_stats(resource_monitor_stats)

      while True:
        with placeholder.container():
          st.title('Resource Monitoring Dashboard')
          try:
            resource_monitor_stats = self.database_handler.get_resource_stats(unique_id)
            cpu_related_info_tab, disk_related_info_tab, memory_related_info_tab, network_related_info_tab, swapped_memory_related_info_tab, process_related_info_tab = self.tabs.get_tabs()

            # Show the tabs
            with cpu_related_info_tab:
              # Show the CPU stats
              self.show_cpu_stats(
                cpu_related_info=resource_monitor_stats["cpu_info"]
              )
            
            with disk_related_info_tab:
              # Show the disk stats
              self.show_disk_stats(
                disk_related_info=resource_monitor_stats["disk_info"]
              )
            
            with memory_related_info_tab:
              # Show the memory stats
              self.show_memory_stats(
                memory_related_info=resource_monitor_stats["memory_info"]
              )
            
            with network_related_info_tab:
              # Show the network stats
              self.show_network_stats(
                network_related_info=resource_monitor_stats["network_info"]
              )

            with swapped_memory_related_info_tab:
              # Show the swapped memory stats
              self.show_swapped_memory_stats(
                swapped_memory_related_info=resource_monitor_stats["swap_memory_info"]
              )

            with process_related_info_tab:
              # Show the process stats
              self.show_process_stats(
                process_related_info=resource_monitor_stats["list_of_processes"][:10]
              )  

          except Exception as e:
            print(e)

          finally:
            pass
          sleep(1)
    
    elif unique_id:
      # Show the error only if user has entered the unique id else show nothing
      st.write('Invalid Unique ID')