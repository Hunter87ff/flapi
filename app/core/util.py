"""
This module contains utility functions that are used in the main module.
"""


# import string
# from pydantic import BaseModel, Field
from typing import Dict, List, Any
from faker import Faker
import random
import re


class DataGenerator:
    DOMAINS = [
        "gmail.com",
        "yahoo.com",
        "outlook.com",
        "hotmail.com",
        "sprucbot.tech"
    ]

    def __init__(self):
        self.fake = Faker()

    def generate_mobile_number(self, country_code:int=91) -> str:
        """
        Generate a random mobile number.
        
        :return: Random mobile number
        """
        _number_prefix = random.choice([62,86,87,88,89,90,91,92,93,94,95,96,97,98,99])
        return f"+{country_code}-{_number_prefix}{random.randint(10_000_000, 99999999)}"


    def generate_value(self, type_spec: str) -> Any:
        match = re.match(r'(\w+)(?::(\d+))?', type_spec)
        if not match:
            raise ValueError(f"Invalid type specification: {type_spec}")
        
        base_type, length = match.groups()
        length = int(length) if length else 5
        if length > 20: length = 20

        if base_type == 'int':
            return random.randint(1, 10**length)
        elif base_type == 'str':
            return self.fake.text(max_nb_chars=length)[:length]
        elif base_type == 'email':
            return self.fake.email(domain=random.choice(self.DOMAINS))
        elif base_type == "name":
            return self.fake.name()
        elif base_type == "address":
            return self.fake.address()
        elif base_type == "date":
            return self.fake.date("%d-%m-%Y")
        elif base_type == "company":
            return self.fake.company()
        elif base_type == "password":
            return self.fake.password(length=length or 8)
        elif base_type == "phone":
            return self.generate_mobile_number()
        else:
            raise ValueError(f"Unsupported type: {base_type}")



    def generate_list(self, list_spec: str) -> List[Any]:
        """
        Generate a list based on the provided specification.
        
        :param list_spec: Specification string
        :return: Generated list
        """
        # Parse list specification
        if '-list-int' in list_spec:
            # Simple list of integers
            amount = int(list_spec.split('-')[0])
            return [random.randint(1, 1000) for _ in range(amount)]
        
        if '-list-str' in list_spec:
            # Simple list of strings
            amount = int(list_spec.split('-')[0])
            return [self.fake.text(max_nb_chars=10) for _ in range(amount)]
        

        
        # List of dictionaries
        amount_match = re.match(r'(\d+)-list-dict\[(.*)\]', list_spec)
        if amount_match:
            amount = int(amount_match.group(1))
            fields_spec = amount_match.group(2)
            
            # Parse individual field specifications
            fields = re.findall(r'(\w+):(\w+)(?::(\d+))?(?::(\d+))?', fields_spec)
            
            return [
                {field: self.generate_value(f"{field_type}:{length}") 
                 for field, field_type, length, _ in fields}
                for _ in range(amount)
            ]
        
        raise ValueError(f"Invalid list specification: {list_spec}")





    def generate_object(self, schema: Dict[str, str]) -> Dict[str, Any]:
        """
        Generate a dictionary object based on the provided schema.
        
        :param schema: Dictionary containing field names and their types
        :return: Generated object
        """
        obj = {}
        for key, type_spec in schema.items():
            if '-list-' in type_spec:
                obj[key] = self.generate_list(type_spec)
            else:
                obj[key] = self.generate_value(type_spec)
        return obj
