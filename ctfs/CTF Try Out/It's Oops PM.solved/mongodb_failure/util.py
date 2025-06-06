import time

def number_to_bstring(n:int)->str:
    return f"{n:016b}"

def bstring_to_number(bstr:str)->int:
    return int(bstr,2)

def now()->float:
    return time.time()

def parse_response(response:str)->str:

    return response\
    .replace("Output",'')\
    .replace("Input",'')\
    .replace(":",'')\
    .strip()
