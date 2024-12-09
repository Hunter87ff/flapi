GEN_QUERY = """{"name": "name", "age": "int:2", "email": "email"}"""
DEV_GEN_QUERY = """{
  "name" : "name()",
  "email" : "email()",
  "addr" : "str(len=6)",
  "ids" : "list-int(amount=2)",
  "datas" : {
    "_$amount" : 2,
    "name" : "name()",
    "position" : "str(len=5)",
    "clients" : {
        "_$amount" : 2,
        "deal" : "int(len=5)",
        "name" : "name()",
        "email" : "email()"
    }
  }
}"""