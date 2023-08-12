import re


i = 0
with open('./badgelog.psv', 'r') as f:
    for line in f.readlines():
        i+=1

        m = re.search('\d{8}', line)

        if(m):
            print(m)
            print(i)