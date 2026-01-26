# utils.py

import logging
import os
import json
import csv
import pandas as pd

def load_json_file(file_path):
    """Loads a JSON file into a Python dictionary."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError as e:
        logging.error(f"Failed to load JSON file: {e}")
        return None

def save_json_file(file_path, data):
    """Saves a Python dictionary to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        logging.error(f"Failed to save JSON file: {e}")

def load_csv_file(file_path):
    """Loads a CSV file into a pandas DataFrame."""
    try:
        return pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        logging.warning(f"CSV file is empty: {file_path}")
        return None
    except pd.errors.ParserError as e:
        logging.error(f"Failed to parse CSV file: {e}")
        return None

def save_csv_file(file_path, data):
    """Saves a pandas DataFrame to a CSV file."""
    try:
        data.to_csv(file_path, index=False)
    except Exception as e:
        logging.error(f"Failed to save CSV file: {e}")

def get_data_directory():
    """Returns the absolute path to the data directory."""
    return os.path.join(os.path.dirname(__file__), 'data')

def get_output_directory():
    """Returns the absolute path to the output directory."""
    return os.path.join(os.path.dirname(__file__), 'output')