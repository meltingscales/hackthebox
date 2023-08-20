# admin, admin@cybermonday.htb


import requests

bot = requests.session()

bot.get('http://cybermonday.htb/')

response = bot.post(
    "http://cybermonday.htb/login",
    {
        # 'username': "admin",
        'email': "admin@cybermonday.htb",
        'password': 'test',
        'remember': 'on'
    })

print(response)