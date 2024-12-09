# flapi
![Flapi](./assets/img//flapi3.png)

A free to use api for devs to get data of their given api structure. it helps to make development faster without the headache of data collection.


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