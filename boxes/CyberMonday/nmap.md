    ┌─[✗]─[vagrant@parrot]─[~]
    └──╼ $sudo nmap -sS -sC -sV -Pn  10.129.100.78
    [sudo] password for vagrant: 
    Starting Nmap 7.92 ( https://nmap.org ) at 2023-08-20 17:07 BST
    Nmap scan report for 10.129.100.78
    Host is up (0.32s latency).
    Not shown: 997 closed tcp ports (reset)
    PORT     STATE    SERVICE      VERSION
    22/tcp   open     ssh          OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
    | ssh-hostkey: 
    |   3072 74:68:14:1f:a1:c0:48:e5:0d:0a:92:6a:fb:c1:0c:d8 (RSA)
    |   256 f7:10:9d:c0:d1:f3:83:f2:05:25:aa:db:08:0e:8e:4e (ECDSA)
    |_  256 2f:64:08:a9:af:1a:c5:cf:0f:0b:9b:d2:95:f5:92:32 (ED25519)
    80/tcp   open     http         nginx 1.25.1
    |_http-server-header: nginx/1.25.1
    |_http-title: Did not follow redirect to http://cybermonday.htb
    5510/tcp filtered secureidprop
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
