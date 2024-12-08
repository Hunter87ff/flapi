import re


def query_parser(query: str) -> dict:
    """
    Parse query string and return dictionary of key-value pairs
    """
    _match = re.match(r'(\w+)\((.*)\)', query)
    if not _match:
        return {}
    _data = _match.group(2).replace(r"\\", "")
    _data = _data.split("&")
    _data = {re.sub(r"[^a-zA-Z_]", "", str(i.split("=")[0])): i.split("=")[1] for i in _data}
    return _data