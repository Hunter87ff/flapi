# Flapi
![Flapi](./assets/img//flapi3.png)

Flapi (derived from "Fill API") is a free-to-use service tailored for frontend developers. It generates mock data effortlessly based on your custom schemas, speeding up your workflow and simplifying development.

## Why Flapi?

**Fully Customizable Data:** Define your schema, and Flapi fills it in no time.

**Dynamic Multi-Response:** Flapi can generate different responses for the same schema in one call (amount parameter).

**Frontend-Centric Design:** Build and test interfaces without backend dependencies.

**Completely Free:** Designed with developers in mind to make their lives easier.

**Let Flapi fill your API needs for mock data and take your development to the next level!**



<details>
<summary>Example Python Code</summary>

```python

import requests

response = requests.get("https://flapi.sprucbot.tech/v1/gen?amount=2", json={
  "name" : "name()",
  "email" : "email(domain=hg.co)",
  "age" : "age(min=78&max=200)",
  "address" : "address()",
  "created_at" : "date()",
  "phone" : "phone(code=87)",
  "ids" : "list-str(amount=3)",
  
  "employee" : {
    "_$amount" : 2,
    "name" : "name()",
    "position" : "text(len=5)",
    "clients" : {
        "_$amount" : 3,
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

</details>




## Example Schema - Response

**Endpoint**
> /v1/gen?amount=2

**Schema**
```json
{
  "name" : "name()",
  "email" : "email(domain=hg.co)",
  "age" : "age(min=78&max=200)",
  "address" : "address()",
  "created_at" : "date()",
  "phone" : "phone(code=87)",
  "ids" : "list-str(amount=3)",
  
  "employee" : {
    "_$amount" : 2,
    "name" : "name()",
    "position" : "text(len=5)",
    "clients" : {
        "_$amount" : 3,
        "deal" : "int(len=5)",
        "name" : "name()",
        "email" : "email(domain=hg.co)"
    }
  }
}
```

<details>
<summary>Response</summary>


```json
{
  "name": "Cindy Bishop",
  "email": "zwhitaker@hg.co",
  "age": 168,
  "address": "109 Howard Gateway\nLake Virginia, PR 82965",
  "created_at": "06-03-1998",
  "phone": "+87-9528360459",
  "ids": [
    "Result.",
    "Their.",
    "Open."
  ],
  "employee": [
    {
      "name": "James Franco",
      "position": "Gas.",
      "clients": [
        {
          "deal": 20410,
          "name": "Christopher Jones",
          "email": "oconnorjerry@hg.co"
        },
        {
          "deal": 81891,
          "name": "Victor Mason",
          "email": "ishepherd@hg.co"
        },
        {
          "deal": 51615,
          "name": "George Parsons",
          "email": "lindsayharvey@hg.co"
        }
      ]
    },
    {
      "name": "Jacob Beltran",
      "position": "Air.",
      "clients": {
        "deal": 30514,
        "name": "Susan Stark",
        "email": "garciajames@hg.co"
      }
    }
  ]
}
```
</details>



## Alternatives to Flapi

### 1. Mockaroo

Allows schema-based data generation.

Has a GUI to define schemas but is not API-first and limited without a paid plan.



### 2. JSONPlaceholder

Provides static, pre-defined mock data.

Cannot generate dynamic data based on custom schemas.



### 3. Faker.js / FakerPy

A library (not an API) for generating fake data programmatically.

Requires setup and coding; no direct schema-to-data API.



### 4. QuickMocker

API mocking platform.

Focused on mocking responses, not dynamic data generation.
