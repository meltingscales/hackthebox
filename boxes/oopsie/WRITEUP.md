# Writeup

## Versions

- Apache httpd 2.4.29 ((Ubuntu))
- Linux OS

## Vuln research

- <https://httpd.apache.org/security/vulnerabilities_24.html>

## Web browsing

### Google Chrome

- Says "Please login to get access to the service" on <http://10.10.10.28/#>.

What does network panel say?

This link <http://10.10.10.28/cdn-cgi/login/script.js> looks suspicious but is empty in Chrome.

Let's try going to <http://10.10.10.28/cdn-cgi/login>.

I used the uname+pw `admin:MEGACORP_4dm1n!!` to get in. I got the password from the previous box, 'archetype' (as this is the starting point lab.)

#### <http://10.10.10.28/cdn-cgi/login/admin.php?content=accounts&id=1>
34322	admin	admin@megacorp.com

### Cookies

I realize that the HTTP requests look like this:

```
GET /cdn-cgi/login/admin.php?content=accounts&id=1 HTTP/1.1
Host: 10.10.10.28
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://10.10.10.28/cdn-cgi/login/admin.php
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: user=34322; role=admin
Connection: close
```

Holy crap. There's no session token! The Cookie contains all of the User ID information!

If I try to go to <http://10.10.10.28/cdn-cgi/login/admin.php?content=uploads>, I get the message,

> This action require super admin rights.

If I change my cookie with Burp Suite, I might be able to get different responses.

I noticed that if I change the `user` cookie to something other than `34322`, I get logged out, but if I change the `role`, nothing happens.

Try `

### dirb http://10.10.10.28/

```
-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Tue Mar  9 22:27:04 2021
URL_BASE: http://10.10.10.28/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://10.10.10.28/ ----
==> DIRECTORY: http://10.10.10.28/css/                                         
==> DIRECTORY: http://10.10.10.28/fonts/                                       
==> DIRECTORY: http://10.10.10.28/images/                                      
+ http://10.10.10.28/index.php (CODE:200|SIZE:10932)                           
==> DIRECTORY: http://10.10.10.28/js/                                          
+ http://10.10.10.28/server-status (CODE:403|SIZE:276)                         
==> DIRECTORY: http://10.10.10.28/themes/                                      
==> DIRECTORY: http://10.10.10.28/uploads/                                     
                                                                               
---- Entering directory: http://10.10.10.28/css/ ----
                                                                               
---- Entering directory: http://10.10.10.28/fonts/ ----
                                                                               
---- Entering directory: http://10.10.10.28/images/ ----
                                                                               
---- Entering directory: http://10.10.10.28/js/ ----
                                                                               
---- Entering directory: http://10.10.10.28/themes/ ----
                                                                               
---- Entering directory: http://10.10.10.28/uploads/ ----
                                                                               
-----------------
END_TIME: Tue Mar  9 22:42:51 2021

```

## nmap

### sudo nmap 10.10.10.28 -sV -sC

```
Starting Nmap 7.91 ( https://nmap.org ) at 2021-03-09 22:24 CST
Nmap scan report for 10.10.10.28
Host is up (0.030s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 61:e4:3f:d4:1e:e2:b2:f1:0d:3c:ed:36:28:36:67:c7 (RSA)
|   256 24:1d:a4:17:d4:e3:2a:9c:90:5c:30:58:8f:60:77:8d (ECDSA)
|_  256 78:03:0e:b4:a1:af:e5:c2:f9:8d:29:05:3e:29:c9:f2 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Welcome
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.52 seconds
```

### nmap -sS -A 10.10.10.28

```
Starting Nmap 7.91 ( https://nmap.org ) at 2021-03-06 20:40 CST
Nmap scan report for 10.10.10.28
Host is up (0.034s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 61:e4:3f:d4:1e:e2:b2:f1:0d:3c:ed:36:28:36:67:c7 (RSA)
|   256 24:1d:a4:17:d4:e3:2a:9c:90:5c:30:58:8f:60:77:8d (ECDSA)
|_  256 78:03:0e:b4:a1:af:e5:c2:f9:8d:29:05:3e:29:c9:f2 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Welcome
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.91%E=4%D=3/6%OT=22%CT=1%CU=41013%PV=Y%DS=2%DC=T%G=Y%TM=60443D1F
OS:%P=x86_64-pc-linux-gnu)SEQ(SP=106%GCD=1%ISR=10B%TI=Z%CI=Z%II=I%TS=A)OPS(
OS:O1=M54DST11NW7%O2=M54DST11NW7%O3=M54DNNT11NW7%O4=M54DST11NW7%O5=M54DST11
OS:NW7%O6=M54DST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)ECN(
OS:R=Y%DF=Y%T=40%W=FAF0%O=M54DNNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS
OS:%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=
OS:Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=
OS:R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T
OS:=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=
OS:S)

Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 143/tcp)
HOP RTT      ADDRESS
1   28.60 ms 10.10.14.1
2   28.70 ms 10.10.10.28

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.34 seconds
```