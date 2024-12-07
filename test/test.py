from faker import Faker
import random
import datetime
import json
import re 



# this is a demo structure. not the general purpose structure
structure = {
    "personal" : "dict[name:str:20, dob:date, email:str:30]",
    "academics" : "dict[class:int:2, section:alphabet:1, roll:int:3, marks:2-list-dict[subject:str:20, score:int:2]]",
    "notices" : "2-list-dict[ title:str:30, date:date, description:str:100]",
    "exams" : "3-list-dict[subject:str:30, date:date, time:time]",
}


class Generator:
    def gen_list(self, val):
        matches = re.match(r'(\d+)-list-(\w+)-(\d+)', val)
        if matches:
            amount = int(matches.group(1))
            data_type = matches.group(2)
            length = int(matches.group(3))
            if data_type == "str":
                return [Faker().text(max_nb_chars=length) for _ in range(amount)]
            elif data_type == "int":
                return [random.randint(1, 10**length) for _ in range(amount)]
            elif data_type == "date":
                return [Faker().date("%d-%m-%Y") for _ in range(amount)]
            elif data_type == "time":
                return [Faker().time() for _ in range(amount)]
            elif data_type == "dict":
                return [self.gen_dict(length) for _ in range(amount)]
            else:
                raise ValueError(f"Unsupported data type: {data_type}")
        else:
            raise ValueError(f"Invalid list specification: {val}")



    def gen_dict(self, structure: dict):
        fake = Faker()
        data = {}
        for key, value in structure.items():
            print(key, value)
            if "str" in value:
                data[key] = fake.text(max_nb_chars=10)
            elif "int" in value:
                data[key] = random.randint(1, 1000)
            elif "date" in value:
                data[key] = fake.date("%d-%m-%Y")
            elif "time" in value:
                data[key] = fake.time()
            elif "list" in value:
                data[key] = self.gen_list(value)
        return data



    def generate_data(self, structure: str):
        fake = Faker()
        data = {}
        for key, value in structure.items():
            print(key, value)
            if "str" in value:
                data[key] = fake.text(max_nb_chars=10)
            elif "int" in value:
                data[key] = random.randint(1, 1000)
            elif "date" in value:
                data[key] = fake.date("%d-%m-%Y")
            elif "time" in value:
                data[key] = fake.time()
            elif "list" in value:
                data[key] = self.gen_list(value)
            elif "dict" in value:
                data[key] = self.gen_dict(value)


    def gen_list_dict(self, val=_exams):
        _match = re.match(r'(\d+)-list-dict\[(.*)\]', val)
        if _match:
            amount = int(_match.group(1))
            fields_spec = _match.group(2)
            fields = fields_spec.split(", ")
            result = []
            for _ in range(amount):
                print(fields)
                result.append(self.generate_data(fields))
            return result
    


print(Generator().generate_data(structure))







