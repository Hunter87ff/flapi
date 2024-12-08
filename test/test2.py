import random, time, re, datetime, string
from faker import Faker
pattern = "date(type=past&format=%d-%m-%y)"
faker = Faker()


def query_parser(query: str) -> dict:
    """
    Parse query string and return dictionary of key-value pairs
    """
    # sanitize query
    _match = re.match(r'(\w+)\((.*)\)', query)
    if not _match:
        return {}
    _data = _match.group(2).replace(r"\\", "")
    _data = _data.split("&")
    _data = {re.sub(r"[^a-zA-Z_]", "", str(i.split("=")[0])): i.split("=")[1] for i in _data}
    return _data

def gen_static(data: str):
    try:
        data = data.split(":")
        if data[0] == "str":
            return faker.text(
                max_nb_chars=int(data[2])
            )
        elif data[0] == "int":
            length = int(data[2])
            return random.randint(10**(length-1), (10**length)-1)
        elif data[0] == "time":
            return datetime.datetime.now().time()
        elif data[0] == "date":
            return faker.date()
        elif data[0] == "alphabet":
            return random.choice(string.ascii_uppercase)
        elif data[0] == "email":
            return faker.email()
        elif data[0] == "name":
            return faker.name()
        else:return "Invalid Data Type"
    except Exception as e:
        return "Invalid Data Type"


def gen_list_dict(data: str=None):
    """
    structure = 2-list-dict[subject:str:20, score:int:2]
    """
    data = "2-list-dict[subject:str:20, score:int:2]"
    _match = re.match(r"(\d+)-list-dict\[(.*)\]", data)
    print(_match.groups())



gen_list_dict()

def gen_dict(data: str=None):
    """
    data = "dict(name=name&email=email, subs=2-list-dict[subject:str:20, score:int:2])"
    """
    _static = ["name", "email", "str", "int"]
    data = "dict(name=name&email=email&subs=2-list-dict[subject:str:20, score:int:2])"
    _data = query_parser(data)
    print(_data)
    _result = {}

    for key, value in _data.items():
        if value.split(":")[0] in _static:
            _result[key] = gen_static(value)

    print(_result)
    



gen_dict()
