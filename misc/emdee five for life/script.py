import requests
import bs4
from bs4 import BeautifulSoup
import hashlib

url = 'http://157.245.39.76:30560'

bot = requests.session()

r = bot.get(url)

print(r)
print(r.text)

soup = BeautifulSoup(r.text,features='lxml')
found = soup.find('h3')

hashme = found.text

print("hash = {}".format(hashme))

hashed = hashlib.md5(hashme.encode('utf-8')).hexdigest()

print("hashed = {}".format(hashed))

data = {'hash': hashed}

response = bot.post(url, data)

print(response)
print(response.text)