"""
This module contains utility functions that are used in the main module.
"""


import traceback
import random, datetime,re
from faker import Faker
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



    @staticmethod
    def gen_static(query:str):
        """
        Generate static data based on the provided query
        """
        if isinstance(query, int):
            return query
        if('list' in query):
            return  Gen.gen_list(query.replace("list-", ""))
        _data:dict =  Gen.query_parser(query)
        _type = _data["type"]
        if(_type=="name"):
            return _faker.name()
        elif(_type=="email"):
            return _faker.email(domain=_data.get("domain", "gmail.com"))
        elif(_type=="password"):
            return _faker.password(length=_data.get("len", 8))
        elif(_type=="text" or _type=="str"):
            return _faker.text(max_nb_chars=int(_data.get("len", 3)))
        elif(_type=="int"):
            length = int(_data.get("len", 3))
            return random.randint(10**(length-1), (10**length)-1)
        elif(_type=="time"):
            return datetime.datetime.now().time()
        elif(_type=="date"):
            return _faker.date("%d-%m-%Y")
        elif _type=="address":
            return _faker.address()
        elif _type=="company":
            return _faker.company()
        elif _type=="phone":
            return Gen.generate_mobile_number(country_code=_data.get("code", 91))
        elif _type=="bool":
            return random.choice([True, False])
        elif _type=="float":
            return random.uniform(1, 100)
        elif _type=="age":
            return random.randint(int(_data.get("min",1)), int(_data.get("max", 100)))
        return "Invalid type"
        


    def gen_list(q):
        _data:dict = Gen.query_parser(q)
        _type = _data.get("type")
        if(_type=="int"):
            amount = int(_data.get("amount", 3))
            return [random.randint(int(_data.get("min", 1)), int(_data.get("max", 100))) for _ in range(amount)]
        elif _type=="str":
            amount = int(_data.get("amount", 3))
            return [_faker.text(max_nb_chars=10) for _ in range(amount)]
        elif _type=="name":
            amount = int(_data.get("amount", 2))
            return [_faker.name() for _ in range(amount)]
        elif _type=="email":
            amount = int(_data.get("amount", 2))
            return [_faker.email(domain=_data.get("domain", "gmail.com")) for _ in range(amount)]
        return []
        
        
        
    def gen_dict(data:dict[str]):
        """
        Best case = O(n) cause we are iterating over the dict only once
        Worst case = O(n^2) but still better than the previous one 
        """
        _copy = data.copy()
        for k, v in data.items():
            if(isinstance(v, dict)):
                _amount = v.get("_$amount")
                if _amount:
                    _copy[k] = [ Gen.gen_dict(v) for _ in range(_amount)]
                else : _copy[k] =  Gen.gen_dict(v)
            else:
                _copy[k] =  Gen.gen_static(v)
        del data
        return _copy

    
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


