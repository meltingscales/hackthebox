#!/usr/bin/env python3

from subprocess import Popen, PIPE

process = Popen(['./baby'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
process.communicate(input=b'password\n')
stdout, stderr = process.communicate()
print (stdout)