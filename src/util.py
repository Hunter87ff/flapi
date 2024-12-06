"""
This module contains utility functions that are used in the main module.
"""


import string
from pydantic import BaseModel, Field
from typing import Dict, List, Any, Union
from faker import Faker
import random
import re

class DataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_value(self, type_spec: str) -> Any:
        # Parse type specification
        match = re.match(r'(\w+)(?::(\d+))?', type_spec)
        if not match:
            raise ValueError(f"Invalid type specification: {type_spec}")
        
        base_type, length = match.groups()
        length = int(length) if length else 10

        # Type-based generation
        if base_type == 'int':
            return random.randint(1, 10**length)
        elif base_type == 'str':
            return self.fake.text(max_nb_chars=length)
        elif base_type == 'email':
            return self.fake.email()
        else:
            raise ValueError(f"Unsupported type: {base_type}")

    def generate_list_dict(self, list_spec: str) -> List[Dict]:
        # Parse list-dict specification
        fields = re.findall(r'(\w+):(\w+)(?::(\d+))?(?::(\d+))?', list_spec)
        
        # Determine list length (default 2)
        list_length_match = re.search(r'\[.*:(\d+)\]', list_spec)
        list_length = int(list_length_match.group(1)) if list_length_match else 2

        return [
            {field: self.generate_value(f"{field_type}:{length}") 
             for field, field_type, length, _ in fields}
            for _ in range(list_length)
        ]

    def generate_object(self, schema: Dict[str, str]) -> Dict[str, Any]:
        obj = {}
        for key, type_spec in schema.items():
            if type_spec.startswith('list-dict'):
                # Extract list-dict specification
                list_spec = type_spec.split('[')[1].rstrip(']')
                obj[key] = self.generate_list_dict(list_spec)
            else:
                obj[key] = self.generate_value(type_spec)
        return obj
