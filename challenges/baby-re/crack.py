#!/usr/bin/env python3

from subprocess import Popen, PIPE
from pprint import pprint

def try_password(input):
    process = Popen(['./baby'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    process.communicate(input=input)
    stdout, stderr = process.communicate()

input = b'(.*)'

# range of all bytes
for i in range(1, 256):
    input += i.to_bytes(1,'big')

input += b'\n'

print("input:")
pprint(input)

process = Popen(['./baby'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate(input=input)
print (stderr.decode('utf-8'))
print (stdout.decode('utf-8'))