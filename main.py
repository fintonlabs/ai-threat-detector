import pandas as pd
from scapy.all import rdpcap

class DataProcessor:
    """
    A class used to process network traffic data from different file formats.
    """

    @staticmethod
    def from_pcap(file_path: str) -> pd.DataFrame:
        """
        Reads network traffic data from a PCAP file and returns a DataFrame.

        Parameters:
        file_path (str): The path to the PCAP file.

        Returns:
        pd.DataFrame: A DataFrame containing the network traffic data.
        """
        packets = rdpcap(file_path)
        data = []

        for packet in packets:
            row = {
                'src_ip': packet[IP].src,
                'dst_ip': packet[IP].dst,
                'src_port': packet[TCP].sport,
                'dst_port': packet[TCP].dport,
                'protocol': packet[IP].proto,
                'payload': packet[TCP].payload
            }
            data.append(row)

        return pd.DataFrame(data)

    @staticmethod
    def from_csv(file_path: str) -> pd.DataFrame:
        """
        Reads network traffic data from a CSV file and returns a DataFrame.

        Parameters:
        file_path (str): The path to the CSV file.

        Returns:
        pd.DataFrame: A DataFrame containing the network traffic data.
        """
        return pd.read_csv(file_path)

    @staticmethod
    def from_json(file_path: str) -> pd.DataFrame:
        """
        Reads network traffic data from a JSON file and returns a DataFrame.

        Parameters:
        file_path (str): The path to the JSON file.

        Returns:
        pd.DataFrame: A DataFrame containing the network traffic data.
        """
        return pd.read_json(file_path)