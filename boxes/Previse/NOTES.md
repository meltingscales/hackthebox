## Info

Attacker IP:    10.10.14.40
Victim IP:      10.10.11.104

## Recon

    ┌─[vagrant@parrot]─[~]
    └──╼ $    nmap -sC -sV 10.10.11.104
    Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-31 19:26 GMT
    Nmap scan report for 10.10.11.104
    Host is up (0.043s latency).
    Not shown: 998 closed tcp ports (conn-refused)
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 53:ed:44:40:11:6e:8b:da:69:85:79:c0:81:f2:3a:12 (RSA)
    |   256 bc:54:20:ac:17:23:bb:50:20:f4:e1:6e:62:0f:01:b5 (ECDSA)
    |_  256 33:c1:89:ea:59:73:b1:78:84:38:a4:21:10:0c:91:d8 (ED25519)
    80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
    |_http-server-header: Apache/2.4.29 (Ubuntu)
    | http-title: Previse Login
    |_Requested resource was login.php
    | http-cookie-flags: 
    |   /: 
    |     PHPSESSID: 
    |_      httponly flag not set
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 9.22 seconds

Created by <https://m4lwhere.org/>

## HTTP

### Fuzzing paths

#### wfuzz dirsearch.txt

    wfuzz --sc 200 -w ~/Git/SecLists/Discovery/Web-Content/dirsearch.txt http://10.10.11.104/FUZZ

    Target: http://10.10.11.104/FUZZ
    Total requests: 13192

    =====================================================================
    ID           Response   Lines    Word       Chars       Payload      
    =====================================================================

    000004848:   200        0 L      0 W        0 Ch        "config.php" 
    000005117:   200        16 L     58 W       939 Ch      "css/"       
    000006046:   200        9 L      54 W       15400 Ch    "favicon.ico"
    000006228:   200        5 L      14 W       217 Ch      "footer.php" 
    000006774:   200        20 L     64 W       980 Ch      "header.php" 
    000007427:   200        17 L     70 W       1155 Ch     "js/"        
    000007785:   200        53 L     138 W      2224 Ch     "login.php"  

Not really useful... `config.php` returns an empty page, perhaps it would be useful later.

#### wfuzz directory-list-2.3-big.txt

    wfuzz --sc 200 -w ~/Git/SecLists/Discovery/Web-Content/directory-list-2.3-big.txt http://10.10.11.104/FUZZ

    TODO

#### dirb

    dirb http://10.10.11.104/

    TODO