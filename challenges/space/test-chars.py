#!/usr/bin/env python3

from subprocess import Popen, PIPE
from pprint import pprint
from typing import Tuple

def send_stdin(input)->Tuple[str,str]:
    process = Popen(['./space'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    process.communicate(input=input)
    stdout, stderr = process.communicate()
    return (stdout,stderr)


# range of all bytes
for i in range(1, 256):
    input = b''
    input += i.to_bytes(1,'big')

    stdout,stderr = send_stdin(input)


print("input:")
pprint(input)
