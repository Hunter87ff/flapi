import re, random

def query_parser(query: str) -> dict:
    """
    Parse query string and return dictionary of key-value pairs
    """
    query = str(query)
    _data:dict = {}
    _match = re.match(r'(\w+)\((.*)\)', query)
    if not _match:
        return {}
    _type = _match.group(1)
    _payload = _match.group(2).replace(r"\\", "")
    _payload = _payload.split("$")
    if _payload[0]!='': _data = {re.sub(r"[^a-zA-Z_]", "", str(i.split("=")[0])): i.split("=")[1] for i in _payload}
    _data["type"] = _type
    return _data

d = {
    "books" : "list(content=int$amount=5$min=4$max=10)",
}

def list_gen(data:dict) -> list:
    data = query_parser(data)
    amount = int(data.get("amount", 1))
    list_gen_list = {
        "int" : lambda: random.randint(int(data.get("min", 0)), int(data.get("max", 100))),
    }
    return [list_gen_list[data.get("content")]() for _ in range(amount)]



def gen_static(query: str):
    """
    Generate static data based on the provided query
    """
    if isinstance(query, int):
        return query
    if 'list' in query:
        return list_gen(query.replace("list-", ""))

