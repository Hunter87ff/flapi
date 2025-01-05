# This one seems like more efficient 
# there will be a web app too, for generating schema 
import re, random, datetime
from faker import Faker

d = {
  "name" : "name()",
  "email" : "email()",
  "addr" : "str(len=6)",
  "ids" : "list-int(amount=2)",
  "datas" : {
    # "_$amount" : 2,
    "name" : "name()",
    "position" : "str(len=5)",
    "clients" : {
        # "_$amount" : 2,
        "deal" : "int(len=5)",
        "name" : "name()",
        "email" : "email()"
    }
  }
}

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
    _payload = _payload.split("&")
    if _payload[0]!='': _data = {re.sub(r"[^a-zA-Z_]", "", str(i.split("=")[0])): i.split("=")[1] for i in _payload}
    _data["type"] = _type
    return _data


class Gen:
    def gen_static(q:str):
        if isinstance(q, int):
            return q
        if('list' in q):
            return  Gen.gen_list(q.replace("list-", ""))
        _data =  query_parser(q)
        _type = _data["type"]
        if(_type=="name"):
            return Faker().name()
        elif(_type=="email"):
            return Faker().email()
        elif(_type=="str"):
            return Faker().text(max_nb_chars=int(_data.get("len", 5)))
        elif(_type=="int"):
            length = int(_data["len"])
            return random.randint(10**(length-1), (10**length)-1)
        elif(_type=="time"):
            return datetime.datetime.now().time()
        


    def gen_list(q):
        _data:dict = query_parser(q)
        _type = _data.get("type")
        if(_type=="int"):
            amount = int(_data.get("amount", 5))
            return [random.randint(1, 1000) for _ in range(amount)]
        elif _type=="str":
            amount = int(_data.get("amount", 5))
            return [Faker().text(max_nb_chars=10) for _ in range(amount)]
        elif _type=="name":
            amount = int(_data.get("amount", 5))
            return [Faker().name() for _ in range(amount)]
        elif _type=="email":
            amount = int(_data.get("amount", 5))
            return [Faker().email(domain=_data.get("domain", "gmail.com")) for _ in range(amount)]
        return []
        
        
        
    def gen_dict(d:dict[str]):
        """
        Best case = O(n) cause we are iterating over the dict only once
        Worst case = O(n^2) but still better than the previous one 
        """
        _copy = d.copy()
        for k, v in d.items():
            if(isinstance(v, dict)):
                _amount = v.get("_$amount")
                if _amount:
                    _copy[k] = [ Gen.gen_dict(v) for _ in range(_amount)]
                else : _copy[k] =  Gen.gen_dict(v)
            else:
                _copy[k] =  Gen.gen_static(v)
        return _copy

    
    @staticmethod
    def generate_object(schema: dict, amount:int=1) -> list[dict]:
        """
        Generate an object based on the provided schema.
        
        :param schema: Schema dictionary
        :return: Generated object
        """
        try:
            # schema = json.loads(schema)
            if amount<=1:
                return  Gen.gen_dict(schema)
            return [ Gen.gen_dict(schema) for _ in range(amount)]
        except Exception as e:
            return {"error": "Invalid schema"}

# import time
# t = time.time()
# d = Gen.generate_object(d, 4)
# print(d)
# print("Time Taken: ",time.time()-t)
