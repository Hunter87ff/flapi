# flapi
A free to use api for devs to get data of their given api structure. it helps to make development faster without the headache of data collection.



## Use
/v1/gen?amount=2
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
v1/gen?amount=2&schema={ "id": "int:5", "name": "name", "date" : "date", "phone" : "phone", "email": "email", "password": "password:10", "clients": "2-list-dict[name:name:10:2, age:int:2, email:email:10]", "books" : "1-list-dict[name:str:10, id:int:5]", "ids" : "2-list-int" }
```

### Output
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