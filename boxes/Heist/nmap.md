┌─[✗]─[vagrant@parrot]─[~]
└──╼ $sudo nmap -sS -sV 10.10.10.149
[sudo] password for vagrant: 
Starting Nmap 7.92 ( https://nmap.org ) at 2023-08-09 17:56 BST
Stats: 0:00:09 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 1.20% done; ETC: 17:59 (0:02:45 remaining)
Nmap scan report for 10.10.10.149
Host is up (0.11s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE SERVICE       VERSION
80/tcp  open  http          Microsoft IIS httpd 10.0
135/tcp open  msrpc         Microsoft Windows RPC
445/tcp open  microsoft-ds?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 28.21 seconds
