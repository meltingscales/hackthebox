    nmap -sS -sC -sV -Pn 10.10.11.219

    ┌─[✗]─[root@parrot]─[/home/vagrant]
    └──╼ #nmap -sS -sC -sV -Pn 10.10.11.219
    Starting Nmap 7.92 ( https://nmap.org ) at 2023-08-15 14:52 BST
    Nmap scan report for 10.10.11.219
    Host is up (0.25s latency).
    Not shown: 998 closed tcp ports (reset)
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
    | ssh-hostkey: 
    |   3072 20:be:60:d2:95:f6:28:c1:b7:e9:e8:17:06:f1:68:f3 (RSA)
    |   256 0e:b6:a6:a8:c9:9b:41:73:74:6e:70:18:0d:5f:e0:af (ECDSA)
    |_  256 d1:4e:29:3c:70:86:69:b4:d7:2c:c8:0b:48:6e:98:04 (ED25519)
    80/tcp open  http    nginx 1.18.0
    |_http-title: Did not follow redirect to http://pilgrimage.htb/
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 44.83 seconds
