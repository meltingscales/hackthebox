## Issues

### horizontall.htb is an invalid host

Add these entries to `/etc/hosts` (IP may be different):

    10.10.11.105    horizontall.htb
    10.10.11.105    api-prod.horizontall.htb

## Recon

### nmap

    ┌─[✗]─[vagrant@parrot]─[~]
    └──╼ $nmap -sC -sV 10.10.11.105
    Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-30 16:44 GMT
    Nmap scan report for 10.10.11.105
    Host is up (0.16s latency).
    Not shown: 989 closed tcp ports (conn-refused)
    PORT      STATE    SERVICE     VERSION
    22/tcp    open     ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 ee:77:41:43:d4:82:bd:3e:6e:6e:50:cd:ff:6b:0d:d5 (RSA)
    |   256 3a:d5:89:d5:da:95:59:d9:df:01:68:37:ca:d5:10:b0 (ECDSA)
    |_  256 4a:00:04:b4:9d:29:e7:af:37:16:1b:4f:80:2d:98:94 (ED25519)
    80/tcp    open     http        nginx 1.14.0 (Ubuntu)
    |_http-server-header: nginx/1.14.0 (Ubuntu)
    |_http-title: Did not follow redirect to http://horizontall.htb
    1031/tcp  filtered iad2
    4003/tcp  filtered pxc-splr-ft
    5963/tcp  filtered indy
    7512/tcp  filtered unknown
    8045/tcp  filtered unknown
    9418/tcp  filtered git
    21571/tcp filtered unknown
    32768/tcp filtered filenet-tms
    49165/tcp filtered unknown
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 39.37 seconds

There's an HTTP server.

I got lazy and looked at a [writeup](https://infosecwriteups.com/horizontall-hackthebox-walkthrough-13090d7d59a2). Apparently we're supposed to fuzz "virtual hosts".

## subdomain evaluation

May take a while. Can use `sudo iftop -i tun0` to see how much traffic is being sent.

    wfuzz -w ~/Git/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -u horizontall.htb --hc 301 -v -c -H "Host:FUZZ.horizontall.htb"

Request # 000047093 gives us HTTP 200.

In `~/Git/SecLists/Discovery/DNS/subdomains-top1million-110000.txt`, line 47093:

    api-prod

## api-prod.horizontall.htb

Just a blank page that says "welcome".

[Time to fuzz!](https://wfuzz.readthedocs.io/en/latest/user/basicusage.html)

    wfuzz --sc 200 -w ~/Git/SecLists/Discovery/Web-Content/directory-list-1.0.txt http://api-prod.horizontall.htb/FUZZ

### Results

-   /reviews
    -   Some JSON API.
    -   Both `/reviews/1` and `/reviews?id=1` work
-   /admin
    -   "strapi" CMS login, redirects to `/admin/auth/login`

According to the writeup I shamelessly stole the answer from, there's some RCE bug that affects the strapi CMS.

So, going to see if I can find the RCE bug in MSF.

## strapi RCE bug

Well, I googled "MSF strapi" and found an exploit script:

<https://www.exploit-db.com/exploits/50239>

Didn't run it, but reading it, saw they query `/admin/init` for the version to see if the exploit would work.

<http://api-prod.horizontall.htb/admin/init> returns `3.0.0-beta.17.4`:

    {"data":{"uuid":"a55da3bd-9693-4a08-9279-f9df57fd1817","currentEnvironment":"development","autoReload":false,"strapiVersion":"3.0.0-beta.17.4"}}

So, it's vulnerable, and we should be able to exploit this RCE bug.

