# utils.py

import os
import json
import logging
import yaml

from dataclasses import dataclass
from typing import Dict, List, Tuple

logger = logging.getLogger(__name__)

@dataclass
class Config:
    settings: Dict

    def __post_init__(self):
        for key, value in self.settings.items():
            setattr(self, key, value)

def load_config(file_path: str) -> Config:
    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
    except yaml.YAMLError as e:
        logger.error(f'Failed to load config from {file_path}: {e}')
        raise

    return Config(config)

def load_json_file(file_path: str) -> Dict:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        logger.error(f'Failed to load JSON from {file_path}: {e}')
        raise

def ensure_dir(file_path: str) -> None:
    if not os.path.exists(file_path):
        os.makedirs(file_path)