nmap -sC -sV -Pn 10.129.98.9

┌─[vagrant@parrot]─[~/Git/hackthebox/boxes/Keeper]
└──╼ $nmap -sC -sV -Pn 10.129.98.9
Starting Nmap 7.92 ( https://nmap.org ) at 2023-08-14 01:22 BST
Stats: 0:00:04 elapsed; 0 hosts completed (0 up), 0 undergoing Host Discovery
Parallel DNS resolution of 1 host. Timing: About 0.00% done
Stats: 0:00:30 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 50.00% done; ETC: 01:22 (0:00:06 remaining)
Nmap scan report for 10.129.98.9
Host is up (0.10s latency).
Not shown: 985 closed tcp ports (conn-refused)
PORT      STATE    SERVICE         VERSION
20/tcp    filtered ftp-data
22/tcp    open     ssh             OpenSSH 8.9p1 Ubuntu 3ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 35:39:d4:39:40:4b:1f:61:86:dd:7c:37:bb:4b:98:9e (ECDSA)
|_  256 1a:e9:72:be:8b:b1:05:d5:ef:fe:dd:80:d8:ef:c0:66 (ED25519)
80/tcp    open     http            nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
705/tcp   filtered agentx
903/tcp   filtered iss-console-mgr
1069/tcp  filtered cognex-insight
1094/tcp  filtered rootd
1717/tcp  filtered fj-hdnet
2045/tcp  filtered cdfunc
5061/tcp  filtered sip-tls
5431/tcp  filtered park-agent
7070/tcp  filtered realserver
10002/tcp filtered documentum
27000/tcp filtered flexlm0
33899/tcp filtered unknown
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 33.85 seconds