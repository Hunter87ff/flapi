[![](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/hunter87ff)  
![GitHub Release](https://img.shields.io/github/v/release/hunter87ff/flapi?logo=Github&label=Release)
[![Language](https://img.shields.io/static/v1?label=Lang&message=Python&logo=Python&color=blue&logoColor=cyan)](#)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Hunter87ff_flapi&metric=security_rating)](#)

<img class="resp-img" src="https://raw.githubusercontent.com/Hunter87ff/flapi/main/assets/img/flapi.png" alt="Flapi" style="border-radius:5px;"/>

Flapi (derived from "Fill API" term) is a free-to-use service tailored for frontend developers. It generates mock data effortlessly based on your custom schemas, speeding up your workflow and simplifying development.

## Why Flapi?

**Fully Customizable Data:** Define your schema, and Flapi fills it in no time.

**Dynamic Multi-Response:** Flapi can generate different responses for the same schema in one call (amount parameter).

**Frontend-Centric Design:** Build and test interfaces without backend dependencies.

**Completely Free:** Designed with developers in mind to make their lives easier.

**Let Flapi fill your API needs for mock data and take your development to the next level!**


## Example Code
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

## Routes
Base URL: https://flapi.sprucbot.tech/v1/gen
### /v1/gen
Generates mock data based on the provided schema. The schema is passed as a JSON object in the request body. The response will be a JSON object with the generated data. The amount parameter can be used to generate multiple responses with the same schema.

#### Endpoint Parameters

- **amount** - The number of responses to generate. Default: 1.
- **schema** - The schema for the data to generate. instead of schema query parameter, you can pass the schema in the request body.


## Types and Parameters
Types and parameters are used to define the schema for the data you want to generate. Here are the available types and parameters:


### Types
- [**int()**](#int) - Generates a random integer within the specified range.
- [**float()**](#float) - Generates a random float within the specified range.
- [**bool()**](#bool) - Generates a random boolean value.

- [**name()**](#name) - Generates a random name.
- [**email()**](#email) - Generates a random email address with the specified domain.
- [**password()**](#password) - Generates a random password with the specified length.
- [**age()**](#age) - Generates a random age within the specified range.
- [**address()**](#address) - Generates a random address.
- [**date()**](#date) - Generates a random date.
- [**phone()**](#phone) - Generates a random phone number with the specified country code.
- [**text()**](#text) - Generates random text with the specified length.
- [**subject()**](#subject) - Generates a random subject.
- [**description()**](#description) - Generates a random description.
- [**list-int()**](#list-int) - Generates a list of random integers with the specified amount and range.
- [**list-str()**](#list-str) - Generates a list of random strings with the specified amount and length.
- [**object{}**](#object) - Generates an object with the specified keys and types.


## Parameters

### int
- **min** - The minimum value of the integer. Default: 0.
- **max** - The maximum value of the integer. Default: 100.

example : 
```json
{
    "int" : "int(min=5$max=10)"
}
```

### float
- **min** - The minimum value of the float. Default: 0.0
- **max** - The maximum value of the float. Default: 100.0

example : 
```json
{
    "float" : "float(min=5$max=10)"
}
```

### bool
- No parameters.

example : 
```json
{
    "bool" : "bool()"
}
```


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

### password
- **len** - The length of the password. Default: 8.

example : 
```json
{
    "pass" : "password(len=8)"
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
- **between** - The date range. Default: `2000-2024`
- **format** - The date format. Default: `%d/%m/%Y`
- **era** - can be `now` so it will generate the current date. 
example : 
```json
{
    "dob" : "date(between=2000-2006)"
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

### subject
- **category** - The category of the subject. Default: `any`
 - - Categories : 
    - - `computer_science` or `cs`
    - - `science` : Science related subjects
    - - `commerce` : Commerce related subjects
    - - `arts` : Arts related subjects
    - - `engineering` : Engineering related subjects
    - - `medical` : Medical related subjects
    - - `law` : Law related subjects
    - - `any` : any random subject

example :
```json
{
    "subject" : "subject(category=commerce)"
}
```

### description
- **words** - The number of words in the description. Default: 3.

example : 
```json
{
    "description" : "description(words=5)"
}
```

### Image
- **width** - The width of the image. Default: 200.
- **height** - The height of the image. Default: 200.

example : 
```json
{
    "image" : "image(width=300$height=300)"
}
```

## List Types
The list types are used to generate a list of values based on the specified schema. 

### list-int
- **amount** - The number of integers to generate. Default: 3.
- **min** - The minimum value of the integers. Default: 0.
- **max** - The maximum value of the integers. Default: 100.

example : 
```json
{
    "list" : "list-int(amount=2$max=5)"
}
```


### list-str
- **amount** - The number of strings to generate. Default: 3.
- **len** - The length of the strings. Default: 10.

example : 
```json
{
    "list" : "list-str(amount=2$len=5)"
}
```

### list-name
- **amount** - The number of names to generate. Default: 3.

example : 
```json
{
    "list" : "list-name(amount=2)"
}
```

### list-email
- **amount** - The number of email addresses to generate. Default: 3.
- **domain** - The domain of the email addresses. Default: gmail.com.

example : 
```json
{
    "list" : "list-email(amount=2$domain=hg.co)"
}
```

### list-subject
- **amount** - The number of subjects to generate. Default: 3.
- **category** - The category of the subjects. Default: any.

example : 
```json
{
    "list" : "list-subject(amount=2$category=cs)"
}
```


### object
Object type defination is a bit different from others. It requires a key and a type. The key is the name of the object's property, and the type is the schema of the object property's value. The object type can also have the _$amount parameter to generate multiple objects with the same schema.
- **_$amount** - The number of objects to generate. Default: 1.


example : 
```json
{
    "obj" : {
        "_$amount" : 2, 
        "name" : "name()",
        "email" : "email(domain=hg.co)",
        "pass" : "password(len=8)"
    }
}
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or feedback.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Hunter87ff/flapi/blob/main/LICENSE) for more details.
