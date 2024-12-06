# flapi
A free to use api for devs to get data of their given api structure. it helps to make development faster without the headache of data collection.



## Use
/gen?amount=10
```json
{
  "id": "int:5", 
  "name": "name:10", 
  "date" : "date",
  "email": "email:12", 
  "password": "str:16", 
  "clients": "2-list-dict[name:str:10:2, age:int:2, email:email:10]",
  "books" : "1-list-dict[name:str:10, id:int:5]",
  "ids" : "4-list-int"
}
```
or 
```sh
/gen?amount=10&data={"id": "int:5", "name": "name:10", "date" : "date", "email": "email:12", "password": "str:16", "clients": "2-list-dict[name:str:10:2, age:int:2, email:email:10]", "books" : "1-list-dict[name:str:10, id:int:5]", "ids" : "4-list-int"}
```