from pprint import pprint
from pathlib import Path

from ismain import is_main

from .read_data import read_data

if is_main():
    data_directory = Path("data")
    event_data = read_data(data_directory)
    pprint(event_data)