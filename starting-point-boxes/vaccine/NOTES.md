## `nmap 10.10.10.46`

```
┌─[vagrant@vagrant-virtualbox]─[~]
└──╼ $sudo nmap -sC 10.10.10.46
Starting Nmap 7.91 ( https://nmap.org ) at 2021-03-31 13:46 CDT
Nmap scan report for 10.10.10.46
Host is up (0.037s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
| ssh-hostkey: 
|   3072 c0:ee:58:07:75:34:b0:0b:91:65:b2:59:56:95:27:a4 (RSA)
|   256 ac:6e:81:18:89:22:d7:a7:41:7d:81:4f:1b:b8:b2:51 (ECDSA)
|_  256 42:5b:c3:21:df:ef:a2:0b:c9:5e:03:42:1d:69:d0:28 (ED25519)
80/tcp open  http
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: MegaCorp Login

Nmap done: 1 IP address (1 host up) scanned in 3.92 seconds
```

## `dirb`

Not really useful.

```
┌─[vagrant@vagrant-virtualbox]─[~]
└──╼ $dirb http://10.10.10.46/

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Wed Mar 31 13:33:22 2021
URL_BASE: http://10.10.10.46/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://10.10.10.46/ ----
+ http://10.10.10.46/index.php (CODE:200|SIZE:2312)                            
+ http://10.10.10.46/server-status (CODE:403|SIZE:276)                         
                                                                               
-----------------
END_TIME: Wed Mar 31 13:36:19 2021
DOWNLOADED: 4612 - FOUND: 2
```

## 

## http://10.10.10.46/

Login page. Time to try some creds!

None seemed to work.

Tried

    admin:MEGACORP_4dm1n!!
    robert:MEGACORP_4dm1n!!

I also tried setting this cookie value:

    user=34322
    role=admin

But that didn't yield results.

Then, I tried SQLMap, but no dice.

    sqlmap http://10.10.10.46 --forms

    [13:40:15] [WARNING] POST parameter 'password' does not seem to be injectable
    [13:40:15] [ERROR] all tested parameters do not appear to be injectable. Try to increase values for '--level'/'--risk' options if you wish to perform more tests. If you suspect that there is some kind of protection mechanism involved (e.g. WAF) maybe you could try to use option '--tamper' (e.g. '--tamper=space2comment') and/or switch '--random-agent', skipping to the next form
