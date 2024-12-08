from faker import Faker
import random
import datetime
import json
import re 
import string


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

from parser import query_parser

class Generator:
    def __init__(self, structure: dict):
        self.faker = Faker()
        self.structure = structure
        self.static_types = ["name", "email", "str", "int", "date", "time", "alphabet"]


    def gen_date(self, data:str):
        data = data.split(":")
        if data[1] == "dob":
            return self.faker.date_of_birth(minimum_age=18, maximum_age=80)
        elif data[1] == "date":
            return self.faker.date()
        elif data[1] == "past":
            return self.faker.past_date()
        elif data[1] == "future":
            return self.faker.future_date()
        elif data[1] == "today":
            return datetime.date.today()
        else:
            return "Invalid Date Type"

    def gen_static(self, data: str):
        try:
            data = data.split(":")
            if data[1] == "str":
                return self.faker.text(
                    max_nb_chars=int(data[2])
                )
            elif data[1] == "int":
                length = int(data[2])
                return random.randint(10**(length-1), (10**length)-1)
            elif data[1] == "time":
                return datetime.datetime.now().time()
            elif data[1] == "date":
                return self.faker.date()
            elif data[1] == "alphabet":
                return random.choice(string.ascii_uppercase)
            
            else:
                return "Invalid Data Type"
        except Exception as e:
            return "Invalid Data Type"
        
    def gen_dict(self, data: str):
        """
        data = "dict(name=name, dob=dob, email=email, subs=2-list-dict[subject:str:20, score:int:2])"
        """
        data = "dict(name=name, dob=dob, email=email, subs=2-list-dict[subject:str:20, score:int:2])"
        _match = re.match(r"dict\((.*)\)", data)
        print(_match)


structure = {
    "personal" : "dict[name:str:20, dob:date, email:str:30]",
    "academics" : "dict[class:int:2, section:alphabet:1, roll:int:3, marks:2-list-dict[subject:str:20, score:int:2]]",
    "notices" : "2-list-dict[ title:str:30, date:date, description:str:100]",
    "exams" : "3-list-dict[subject:str:30, date:date, time:time]",
}

