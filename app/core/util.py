"""
This module contains utility functions that are used in the main module.
"""


import traceback
import random, datetime,re
from faker import Faker
from core.locale import _datetime
from core.locale._subject import Subject
from ext.error import NotQuery


_faker = Faker()
class Gen:
    """
    Utility class for generating mock data based on the provided schema
    """

    @staticmethod
    def generate_mobile_number(country_code:int=91) -> str:
        """
        Generate a random mobile number.
        
        :return: Random mobile number
        """
        _number_prefix = random.choice([62,86,87,88,89,90,91,92,93,94,95,96,97,98,99])
        return f"+{country_code}-{_number_prefix}{random.randint(10_000_000, 99999999)}"


    @staticmethod
    def query_parser(query: str) -> dict:
        """
        Parse query string and return dictionary of key-value pairs
        """
        try:
            query = str(query)
            _data:dict = {}
            _match = re.match(r'(\w+)\((.*)\)', query)
            if not _match:
                return {}
            _type = _match.group(1)
            _payload = _match.group(2).replace(r"\\", "")
            _payload = _payload.split("$")
            if _payload[0]!='': _data = {re.sub(r"[^a-zA-Z_]", "", str(i.split("=")[0])): i.split("=")[1] for i in _payload}
            _data["type"] = _type
            return _data
        except Exception as e:
            raise NotQuery(f"Invalid query format: {query}")


    @staticmethod
    def gen_static(query: str):
        """
        Generate static data based on the provided query
        """
        if isinstance(query, int):
            return query
        if 'list' in query:
            return Gen.gen_list(query.replace("list-", ""))

        try:
            _data: dict = Gen.query_parser(query)
            _type = _data.get("type")
        except Exception as e:
            if isinstance(e, NotQuery):
                return f"Invalid Query Parameters: {query}"
            
        if not _type:
            return query



        # Dictionary mapping types to their generator functions
        type_generators = {
            "name": lambda: _faker.name(),
            "email": lambda: _faker.email(domain=_data.get("domain", "gmail.com")),
            "password": lambda: _faker.password(length=int(_data.get("len", 8))),
            "text": lambda: _faker.text(max_nb_chars=int(_data.get("len", 5))),

            "str": lambda: _faker.text(max_nb_chars=int(_data.get("len", 3))),
            "int": lambda: random.randint(int(_data.get("min",1)), int(_data.get("max", 100))),
            "bool": lambda: random.choice([True, False]),
            "float": lambda: random.uniform(int(_data.get("min",1)), int(_data.get("max", 100))),

            "time": lambda: datetime.datetime.now().time(),
            "date": lambda: _datetime.DateTime.get_date(era=_data.get("era"), format=_data.get("format", "%d/%m/%Y"), between_yr=_data.get("between", "2000-2024")),
            "address": lambda: _faker.address(),
            "company": lambda: _faker.company(),
            "phone": lambda: Gen.generate_mobile_number(country_code=_data.get("code", 91)),

            "age": lambda: random.randint(int(_data.get("min",1)), int(_data.get("max", 100))),
            "description": lambda: _faker.sentence(nb_words=int(_data.get("words", 4))),
            "image": lambda: _faker.image_url(width=int(_data.get("width", 200)), height=int(_data.get("height", 200))),
            "subject": lambda: Subject.get_subject(_data.get("category", "computer_science")),
        }


        return type_generators.get(_type, lambda: query)()


    def gen_list(q):
        _data:dict = Gen.query_parser(q)
        _type = _data.get("type")
        # amount between 1 and 100 only!!
        amount = min(max(int(_data.get("amount", 3)),1), 100)
        type_generators = {
            "int": lambda: [random.randint(int(_data.get("min", 1)), int(_data.get("max", 100))) for _ in range(amount)],
            "str": lambda: [_faker.text(max_nb_chars=10) for _ in range(amount)],
            "name": lambda: [_faker.name() for _ in range(amount)],
            "email": lambda: [_faker.email(domain=_data.get("domain", "gmail.com")) for _ in range(amount)],
            "subject": lambda: [Subject.get_subject(_data.get("category", "any")) for _ in range(amount)],
        }
        return type_generators.get(_type, lambda: "Invalid type")()
        

    #something went wrong within the try block..
    def gen_dict(data: dict[str]) -> dict:
        """
        Generate a dictionary based on the provided schema.

        :param data: A dictionary where keys are strings and values can be either static data or another dictionary.
        :return: A dictionary with generated data based on the provided schema.
        """
        """
        Generate a dictionary based on the provided schema
        """
        _copy = data.copy()
        try:
            # get key and value of the dict
            for k, v in data.items():
                # if the value is a dict
                if(isinstance(v, dict)):
                    # get the amount of the dict
                    _amount = min(max(int(v.get("_$amount", 1)),1), 100)
                    # if the amount is greater than 1, then generate the dict
                    if _amount:
                        
                        _copy[k] = [Gen.gen_dict(v)  for _ in range(_amount) ]
                        #del v["_$amount"]

                    # if the amount is 1, then generate the dict
                    else : 
                        _copy[k] =  Gen.gen_dict(v)
                # if the value is not a dict
                else:
                    # generate the static data
                    _copy[k] =  Gen.gen_static(v)


            # delete the data
            del data
            return _copy

        except Exception as e:
            traceback.print_exc()
            return {"error": str(e)}

    
    @staticmethod
    def generate_object(schema: dict, amount:int=1) -> list[dict]:
        """
        Generate an object based on the provided schema.
        
        :param schema: Schema dictionary
        :return: Generated object
        """
        try:
            if amount<=1:
                return  Gen.gen_dict(schema)
            return [ Gen.gen_dict(schema) for _ in range(amount)]
        except Exception as e:
            traceback.print_exc()
            return {"error": str(e)}


