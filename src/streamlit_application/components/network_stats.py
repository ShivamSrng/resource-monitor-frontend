import pandas as pd
import streamlit as st
import altair as alt


class NetworkStats:
  def __init__(self) -> None:
    self.cnt = 0
    self.dataframe_bytes = pd.DataFrame()
    self.dataframe_packets = pd.DataFrame()

  
  def prepare_for_showing_stats(self, network_related_info: dict) -> None:
    self.dataframe_bytes = pd.DataFrame(columns=["cnt", "bytes_sent", "bytes_recv"])
    self.dataframe_bytes.loc[len(self.dataframe_bytes)] = [self.cnt, network_related_info["bytes_sent"] // (2**20), network_related_info["bytes_recv"] // (2**20)]

    self.dataframe_packets = pd.DataFrame(columns=["cnt", "packets_sent", "packets_recv"])
    self.dataframe_packets.loc[len(self.dataframe_packets)] = [self.cnt, network_related_info["packets_sent"], network_related_info["packets_recv"]]
    self.cnt += 1
  

  def run(self, network_stats: dict) -> None:
    placeholder_network = st.empty()
    self.dataframe_bytes.loc[len(self.dataframe_bytes)] = [self.cnt, network_stats["bytes_sent"] // (2**20), network_stats["bytes_recv"] // (2**20)]
    self.dataframe_packets.loc[len(self.dataframe_packets)] = [self.cnt, network_stats["packets_sent"], network_stats["packets_recv"]]
    self.cnt += 1

    with placeholder_network.container():
      st.subheader('Network Usage')
      st.write("Network Bytes Information")
      st.write("Total number of errors while receiving: ", network_stats["errin"])
      st.write("Total number of errors while sending: ", network_stats["errout"])
      bytes_sent_info, bytes_recv_info = st.columns([0.5, 0.5])
      with bytes_sent_info:
        st.write(f"Bytes Sent: {network_stats['bytes_sent'] // (2**20)} MBPS")
        st.altair_chart(
          alt.Chart(self.dataframe_bytes).mark_area().encode(
            y=alt.Y("bytes_sent", title="Megabytes Sent Per Second"),
            x=alt.X("cnt", title="Time"),
          )
        )

      with bytes_recv_info:
        st.write(f"Bytes Received: {network_stats['bytes_recv'] // (2**20)} MBPS")
        st.altair_chart(
          alt.Chart(self.dataframe_bytes).mark_area().encode(
            y=alt.Y("bytes_recv", title="Megabytes Received Per Second"),
            x=alt.X("cnt", title="Time"),
          )
        )
      
      st.write("Network Packets Information")
      st.write("Total number of errors while receiving: ", network_stats["dropin"])
      st.write("Total number of errors while sending: ", network_stats["dropout"])
      packets_sent_info, packets_recv_info = st.columns([0.5, 0.5])
      
      with packets_sent_info:
        st.write(f"Packets Sent: {network_stats['packets_sent']}")
        st.altair_chart(
          alt.Chart(self.dataframe_packets).mark_area().encode(
            y=alt.Y("packets_sent", title="Packets Sent"),
            x=alt.X("cnt", title="Time"),
          )
        )

      with packets_recv_info:
        st.write(f"Packets Received: {network_stats['packets_recv']}")
        st.altair_chart(
          alt.Chart(self.dataframe_packets).mark_area().encode(
            y=alt.Y("packets_recv", title="Packets Received"),
            x=alt.X("cnt", title="Time"),
          )
        )