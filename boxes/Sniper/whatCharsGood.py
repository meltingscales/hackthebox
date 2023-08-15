import requests
import string
import random

loginurl = "http://10.10.10.151/user/login.php"
registerurl = "http://10.10.10.151/user/registration.php"
# Get all the symbols and add them in a list
characters = string.punctuation
# Pick a random number of characters to fill in the forms
rand = "A"*random.randint(1,10)

print("Blacklisted Characters: ")
# Iterate the list
for char in characters:
    # Keep the single character in a variable
    original = char
    # Fill the username and password with letters
    char = rand+char
    data = {'email':'test@test.test', 'username':char, 'password':char,'submit':' '}
    
    r = requests.post(url = registerurl, data = data)
    data = {'username':char, 'password':char, 'submit':' '}
    r = requests.post(url = loginurl, data = data)
    # Check if we can log in with that specific character in the username
    if" Username/password is incorrect." in r.text:
        print(original)
