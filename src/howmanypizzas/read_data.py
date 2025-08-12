from pathlib import Path
from datetime import datetime
from collections import defaultdict
import csv
import re
from logging import getLogger

log = getLogger(__name__)

def read_data(data_directory: Path) -> dict[datetime, dict[datetime, int]]:
    """
    Reads the data from the file and returns a dictionary with dates as keys and pizza counts as values.

    :param data_directory: Path to the directory containing the CSV files.
    :return: A dictionary where keys are event dates and values are dictionaries with registration dates as keys
             and the number of registrations as values.
    """

    file_name_pattern = re.compile(r'^sf_python_(\d{4})_(\d{1,2})_(\d{1,2})\.csv$')

    registration_data = defaultdict(dict)
    data_file_paths = sorted(data_directory.glob('*.csv'))
    if len(data_file_paths) < 1:
        raise FileNotFoundError(f'No CSV files found in "{data_directory}".')

    for data_file_path in data_file_paths:
        print(data_file_path.name)
        if (file_name_match := file_name_pattern.search(data_file_path.name)) is None:
            continue
        year = int(file_name_match.group(1))
        month = int(file_name_match.group(2))
        day = int(file_name_match.group(3))
        event_date = datetime(year, month, day)

        with data_file_path.open() as file:
            csv_dict_reader = csv.DictReader(file)
            for row in csv_dict_reader:
                date_string = row.get('Date')  # convert yyyy-mm-dd to datetime
                date = datetime.strptime(date_string, '%Y-%m-%d')
                if (registrations := int(row.get('Registrations'))) > 0:
                    registration_data[event_date][date] = registrations

    registration_data = dict(registration_data)

    return registration_data

