# flapi
A free to use api for devs to get data of their given api structure. it helps to make development faster without the headache of data collection.


<details>
<summary>Example Python Code</summary>

```python

import requests

response = requests.get("https://flapi.sprucbot.tech/v1/gen?amount=2", json={
    "id": "int:5", 
    "name": "name", 
    "date" : "date",
    "phone" : "phone",
    "email": "email", 
    "password": "password:10", 
    "clients": "2-list-dict[name:name:10:2, age:int:2, email:email:10]",
    "books" : "1-list-dict[name:str:10, id:int:5]",
    "ids" : "2-list-int"
})

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
  "id": "int:5", 
  "name": "name", 
  "date" : "date",
  "phone" : "phone",
  "email": "email", 
  "password": "password:10", 
  "clients": "2-list-dict[name:name:10:2, age:int:2, email:email:10]",
  "books" : "1-list-dict[name:str:10, id:int:5]",
  "ids" : "2-list-int"
}
```

or 
```sh
# Url Encoded Schema / Raw Json Schema
curl -X 'GET' \
  'http://localhost:8000/v1/gen/?amount=1&schema=%7B%20%22id%22%3A%20%22int%3A2%22%2C%20%22name%22%3A%20%22name%3A10%22%2C%20%22date%22%20%3A%20%22date%22%2C%20%22email%22%3A%20%22email%3A12%22%2C%20%22password%22%3A%20%22str%3A16%22%2C%20%22clients%22%3A%20%222-list-dict%5Bname%3Astr%3A10%3A2%2C%20age%3Aint%3A2%2C%20email%3Aemail%3A10%5D%22%2C%20%22books%22%20%3A%20%221-list-dict%5Bname%3Astr%3A10%2C%20id%3Aint%3A5%5D%22%2C%20%22ids%22%20%3A%20%224-list-int%22%20%7D' \
  -H 'accept: application/json'
```

<details>
<summary>Response</summary>


```json
[
  {
    "id": 30738,
    "name": "Michael Edwards",
    "date": "26-07-1973",
    "phone": "+91-8786127548",
    "email": "hansonsean@yahoo.com",
    "password": ")8UCVDTe%R",
    "clients": [
      {
        "name": "Jason Stanley",
        "age": 43,
        "email": "joseph26@outlook.com"
      },
      {
        "name": "William Fuller",
        "age": 15,
        "email": "ybryant@yahoo.com"
      }
    ],
    "books": [
      {
        "name": "Best hard.",
        "id": 61727
      }
    ],
    "ids": [
      288,
      344
    ]
  },
  {
    "id": 42835,
    "name": "Jennifer King",
    "date": "12-09-2019",
    "phone": "+91-8967457046",
    "email": "thill@gmail.com",
    "password": "j6hi1CoT@)",
    "clients": [
      {
        "name": "Kari Ford",
        "age": 55,
        "email": "marcus82@hotmail.com"
      },
      {
        "name": "Daniel Doyle",
        "age": 6,
        "email": "masonjohn@sprucbot.tech"
      }
    ],
    "books": [
      {
        "name": "Cut money.",
        "id": 58816
      }
    ],
    "ids": [
      555,
      819
    ]
  }
]
```
</details>