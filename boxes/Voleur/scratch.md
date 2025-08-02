ldapdomaindump -u ryan.naylor -p HollowOct31Nyt 10.10.11.76

Not working :(

https://www.hyhforever.top/posts/2025/07/htb-voleur/

...it's just kerberoasting?? cool :)


```bash


VBoxManage setextradata "kali-linux-2025.1c-virtualbox-amd64" "VBoxInternal/Devices/VMMDev/0/Config/GetHostTimeDisabled" 1

sudo su

timedatectl set-ntp off
ntpdate voleur.htb

impacket-getTGT voleur.htb/'ryan.naylor':'HollowOct31Nyt'
export KRB5CCNAME=$(pwd)/ryan.naylor.ccache
nxc ldap voleur.htb -u ryan.naylor -p HollowOct31Nyt -k
nxc smb dc.voleur.htb -u ryan.naylor -p HollowOct31Nyt -k

bloodhound-python -u ryan.naylor -p HollowOct31Nyt -k -ns 10.10.11.76 -c All -d voleur.htb --zip

netexec smb dc.voleur.htb -u ryan.naylor -p 'HollowOct31Nyt' -k --shares --smb-timeout 500

impacket-smbclient -k dc.voleur.htb
    login voleur.htb/ryan.naylor #(DOESNT WORK)

nxc smb 10.10.11.76 -u ryan.naylor -p 'HollowOct31Nyt' -M spider_plus










```

I'm stuck and there are no other writeups. Time to move on.