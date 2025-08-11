from pprint import pprint

from ismain import is_main

from .read_data import read_data

if is_main():
    event_data = read_data()
    pprint(event_data)