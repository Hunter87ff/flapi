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

"""
def gen_statis() -> generate static type data (int, str, date, time etc.) # No Iteration
def gen_list() -> distribute task among other generators ⬆️⬇️ #Have Iteration
def gen_dict() -> distribute task among other generators ⬆️⬇️ #Have Iteration 



# Personal
Enter key -> dict -> call gen_dict(
called gen_static(name:str:20) -> return data -> store in dict with key (name)
called gen_static(dob:date) -> return data -> store in dict with key (dob)
called gen_static(email:str:30) -> return data -> store in dict with key (email)
return dict

# Academics
Enter key -> dict -> call gen_dict(
called gen_static(class:int:2) -> return data -> store in dict with key (class)
called gen_static(section:alphabet:1) -> return data -> store in dict with key (section)
called gen_static(roll:int:3) -> return data -> store in dict with key (roll)
called gen_list(marks:2-list-dict[subject:str:20, score:int:2]) -> called gen_dict(
    called gen_static(subject:str:20) -> return data -> store in dict with key (subject)
    called gen_static(score:int:2) -> return data -> store in dict with key (score)
    return dict
) -> return data -> store in dict with key (marks)
return dict

# Notices
Enter key -> list -> call gen_list(
called gen_dict(title:str:30) -> return data -> store in dict with key (title)
called gen_static(date:date) -> return data -> store in dict with key (date)
called gen_static(description:str:100) -> return data -> store in dict with key (description)
return list
)



"""



class Generator:
    def __init__(self):
        self.faker = Faker()


    def generate_data(self, structure: str):
        fake = self.faker
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


    def gen_list(self, val):
        matches = re.match(r'(\d+)-list-(\w+)-(\d+)', val)
        if matches:
            amount = int(matches.group(1))
            data_type = matches.group(2)
            length = int(matches.group(3))
            if data_type == "str":
                return [self.faker.text(max_nb_chars=length) for _ in range(amount)]
            elif data_type == "int":
                return [random.randint(1, 10**length) for _ in range(amount)]
            elif data_type == "date":
                return [self.faker.date("%d-%m-%Y") for _ in range(amount)]
            elif data_type == "time":
                return [self.faker.time() for _ in range(amount)]
            elif data_type == "dict":
                return [self.gen_dict(length) for _ in range(amount)]
            else:
                raise ValueError(f"Unsupported data type: {data_type}")
        else:
            raise ValueError(f"Invalid list specification: {val}")



    def gen_dict(self, structure: dict):
        fake = self.faker
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



    def gen_list_dict(self, val):
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
    