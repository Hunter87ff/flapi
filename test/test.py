# Structure of data
# data-type : length : words(string)
import random, string

_types = ["int", "float", "str", "email"]
_payload:dict[str:str] = {
    "name" : "str:10",
    "id" : "int:3",
    "email" : "email:10",
}

def generate_int(_length):
    return int(''.join(random.choices(string.digits, k=_length)))

def generate_float(_length):
    return float(''.join(random.choices(string.digits, k=_length)))

def generate_str(_length, _words):
    return ''.join([''.join(random.choices(string.ascii_lowercase, k=_length)) for _ in range(_words)])

def generate_email(_length):
    return ''.join(random.choices(string.ascii_lowercase, k=_length)) + "@gmail.com"




def generate_data(_type, _length, _words=1):
    if _type == "int":
        return generate_int(_length)
    elif _type == "float":
        return generate_float(_length)
    elif _type == "str":
        return generate_str(_length, _words)
    elif _type == "email":
        return generate_email(_length)
    else:
        return ("Invalid data type")



def generate_payload(_payload:dict[str:str], _amount:int=10):
    _obj = []
    for _ in range(_amount):
        _data = {}
        for key in _payload:
            _features = _payload[key].split(":")
            _type = _features[0]
            _length = int(_features[1])
            _words = int(_features[2] if len(_features) > 2 else 1)
            _data[key] = generate_data(_type, _length)
        _obj.append(_data)
    return _obj


def main():
    print(generate_payload(_payload))

if __name__ == "__main__":
    main()