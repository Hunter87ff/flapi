# This one seems like more efficient 

# there will be a web app too, for generating schema 


d = {
  "_$amount" : 2,
  "name" : "name",
  "id" : "int:5",
  #"l" : [8,6,8]
  "d1" : {
    "_$amount" : 3,
    "x" : "str:6",
    "d2" : {
      "x1" : "str:10", 
      "d3":{
        "h":"int:3"
      }
    }
  },
  "datas" : {
    "_$amount" : 5,
    "name" : "name"
  }
}

def it_dict(d, a=1):
  #print(d)
  for i in d.keys():
    print(f"{' '*(a*a)}sub-{a} : {d[i]}" , type(d[i]))
    if(isinstance(d[i], dict)):
      it_dict(d[i], a+1)



for k in d.keys():
  #print(isinstance(d[k], dict))
  if isinstance(d[k], dict):
    it_dict(d[k])
  else: print(d[k], type(d[k]))
