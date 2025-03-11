import pandas as pd
from data_processor import DataProcessor

def test_from_pcap():
    data = DataProcessor.from_pcap('tests/test.pcap')
    assert isinstance(data, pd.DataFrame)

def test_from_csv():
    data = DataProcessor.from_csv('tests/test.csv')
    assert isinstance(data, pd.DataFrame)

def test_from_json():
    data = DataProcessor.from_json('tests/test.json')
    assert isinstance(data, pd.DataFrame)