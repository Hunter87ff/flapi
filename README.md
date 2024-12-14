# Flapi
[![](https://img.shields.io/static/v1?label=Donate&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/hunter87ff)  
![GitHub Release](https://img.shields.io/github/v/release/hunter87ff/flapi?logo=Github&label=Release)
[![Language](https://img.shields.io/static/v1?label=Lang&message=Python&logo=Python&color=blue&logoColor=cyan)](#)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Hunter87ff_flapi&metric=security_rating)](#)

<img src="https://raw.githubusercontent.com/Hunter87ff/flapi/main/assets/img/flapi.png" alt="Flapi" style="width:fit-content; max-width:80%;"/>

Flapi (derived from "Fill API" term) is a free-to-use service tailored for frontend developers. It generates mock data effortlessly based on your custom schemas, speeding up your workflow and simplifying development.

## Why Flapi?

**Fully Customizable Data:** Define your schema, and Flapi fills it in no time.

**Dynamic Multi-Response:** Flapi can generate different responses for the same schema in one call (amount parameter).

**Frontend-Centric Design:** Build and test interfaces without backend dependencies.

**Completely Free:** Designed with developers in mind to make their lives easier.

**Let Flapi fill your API needs for mock data and take your development to the next level!**


## Example Schema - Request Through Python
```python

import requests

response = requests.get(
    "https://flapi.sprucbot.tech/v1/gen?amount=2", 
    json={
        "name" : "name()",
        "email" : "email(domain=hg.co)",
        "age" : "age(min=78$max=200)",
        "address" : "address()",
        "created_at" : "date()",
        "phone" : "phone(code=87)",
        "ids" : "list-int(amount=3$max=2)",
        "employee" : {
            "_$amount" : 1,
            "name" : "name()",
            "position" : "text(len=5)",
            "clients" : {
                "_$amount" : 2,
                "deal" : "int(len=5)",
                "name" : "name()",
                "email" : "email(domain=hg.co)"
            }
        }
    }
)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

```



**Endpoint**
> /v1/gen?amount=2

**Schema**

```json
{
  "name" : "name()",
  "email" : "email(domain=hg.co)",
  "age" : "age(min=78$max=200)",
  "address" : "address()",
  "created_at" : "date()",
  "phone" : "phone(code=87)",
  "ids" : "list-int(amount=3$max=2)",
  "employee" : {
    "_$amount" : 1,
    "name" : "name()",
    "position" : "text(len=5)",
    "clients" : {
        "_$amount" : 2,
        "deal" : "int(len=5)",
        "name" : "name()",
        "email" : "email(domain=hg.co)"
    }
  }
}
```


**Example Response**

```json
{
  "name": "Jennifer Huynh",
  "email": "kristenturner@hg.co",
  "age": 125,
  "address": "959 Holden Corner Apt. 103\nEast Matthew, IN 93214",
  "created_at": "18-12-2003",
  "phone": "+87-9487346280",
  "ids": [1,2,1],
  "employee": [
    {
      "_$amount": 1,
      "name": "Jason Hartman",
      "position": "PM.",
      "clients": [
        {
          "_$amount": 2,
          "deal": 55503,
          "name": "Nicole Parker",
          "email": "yhopkins@hg.co"
        },
        {
          "_$amount": 2,
          "deal": 35965,
          "name": "Mark Thomas",
          "email": "kirsten79@hg.co"
        }
      ]
    }
  ]
}
```


## Types and Parameters
Types and parameters are used to define the schema for the data you want to generate. Here are the available types and parameters:


### Types
- [**name()**](#name) - Generates a random name.
- [**email()**](#email) - Generates a random email address with the specified domain.
- [**age()**](#age) - Generates a random age within the specified range.
- [**address()**](#address) - Generates a random address.
- [**date()**](#date) - Generates a random date.
- [**phone()**](#phone) - Generates a random phone number with the specified country code.
- [**text()**](#text) - Generates random text with the specified length.
- [**list-int()**](#list-int) - Generates a list of random integers with the specified amount and range.
- [**list-str()**](#list-str) - Generates a list of random strings with the specified amount and length.
- [**object{}**](#object) - Generates an object with the specified keys and types.


## Parameters
### name
- No parameters.

example : 
```json
{
    "name" : "name()"
}
```


### email
- **domain** - The domain of the email address. Default: gmail.com.

example : 
```json
{
    "email" : "email(domain=hg.co)"
}
```


### age
- **min** - The minimum age. Default: 18.
- **max** - The maximum age. Default: 100.

example : 
```json
{
    "age" : "age(min=78$max=200)"
}
```


### address
- No parameters.

example : 
```json
{
    "address" : "address()"
}
```


### date
- No parameters.

example : 
```json
{
    "date" : "date()"
}
```


### phone
- **code** - The country code of the phone number. Default: 91.

example : 
```json
{
    "phone" : "phone(code=87)"
}
```


### text
- **len** - The length of the text. Default: 10.

example : 
```json
{
    "text" : "text(len=5)"
}
```


### list-int
Every list and object type can have a **_$amount** parameter to specify the number of items to generate.
- **_$amount** - The number of integers to generate. Default: 5.
- **min** - The minimum value of the integers. Default: 0.
- **max** - The maximum value of the integers. Default: 100.

example : 
```json
{
    "list" : "list-int(amount=2$max=5)"
}
```


### list-str
- **_$amount** - The number of strings to generate. Default: 5.
- **len** - The length of the strings. Default: 10.

example : 
```json
{
    "list" : "list-str(amount=2$len=5)"
}
```


### object
- **_$amount** - The number of objects to generate. Default: 1.
- **<key>** - The key of the object.
- **<type>** - The type of the object.

example : 
```json
{
    "obj" : {
        "_$amount" : 2, //creates a list of 2 objects
        "name" : "name()",
        "email" : "email(domain=hg.co)"
    }
}
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or feedback.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Hunter87ff/flapi/blob/main/LICENSE) for more details.
