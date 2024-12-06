henry@fz-55:~/Git/hackthebox/boxes/Alert$ sudo nmap -sS -sV 10.10.11.44
[sudo] password for henry: 
Starting Nmap 7.92 ( https://nmap.org ) at 2024-12-06 14:49 CST
Nmap scan report for alert.htb (10.10.11.44)
Host is up (0.081s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel


http://alert.htb/visualizer.php - renders MD to HTML

http://alert.htb/visualizer.php?link_share=675360f4da1b57.26570691.md - reads an MD file from the server and lets you view it


# possible vulnerabilities:

## local file inclusion: I can read any file on the disk

http://alert.htb/visualizer.php?link_share=675360f4da1b57.26570691.md
http://alert.htb/visualizer.php?link_share=../../../etc/shadow
http://alert.htb/visualizer.php?link_share=../../../etc/passwd
http://alert.htb/visualizer.php?link_share=675360f4da1b57.26570691.md
http://alert.htb/visualizer.php?link_share=675360f4da1b57.26570691.md

../../../etc/shadow
invalid file name

potato.md
invalid file

/potato.md
invalid file name

~
invalid file name

dev
invalid file name

dev.md
invalid file

## php code injection: run php code

nope.

## link_share=675366f223c3a2.56858265.md - md5 hash?

nope. some unique id.

## burp suite: fiddle with filename parameter. 

Maybe the filename sent by the browser goes directly into a shell.

i.e.

FILENAME="asdf.md"
pandoc --convert "asdf.md" --output "asdf.html"

bad:
FILENAME='evil.md"; sleep 10;"'
pandoc --convert "evil.md"; sleep 10;"" --output "asdf.html"


Payloads that do nothing:
;.md
potato.md
;'.md