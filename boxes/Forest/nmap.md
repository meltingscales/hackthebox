

    ┌─[vagrant@parrot]─[~]
    └──╼ $sudo nmap -sS -sC -sV -Pn 10.10.10.161
    Starting Nmap 7.92 ( https://nmap.org ) at 2023-08-15 00:41 BST
    Nmap scan report for htb.local (10.10.10.161)
    Host is up (0.44s latency).
    Not shown: 989 closed tcp ports (reset)
    PORT     STATE SERVICE      VERSION
    53/tcp   open  domain       Simple DNS Plus
    88/tcp   open  kerberos-sec Microsoft Windows Kerberos (server time: 2023-08-14 23:48:25Z)
    135/tcp  open  msrpc        Microsoft Windows RPC
    139/tcp  open  netbios-ssn  Microsoft Windows netbios-ssn
    389/tcp  open  ldap         Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
    445/tcp  open  microsoft-ds Windows Server 2016 Standard 14393 microsoft-ds (workgroup: HTB)
    464/tcp  open  kpasswd5?
    593/tcp  open  ncacn_http   Microsoft Windows RPC over HTTP 1.0
    636/tcp  open  tcpwrapped
    3268/tcp open  ldap         Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
    3269/tcp open  tcpwrapped
    Service Info: Host: FOREST; OS: Windows; CPE: cpe:/o:microsoft:windows

    Host script results:
    |_clock-skew: mean: 2h26m50s, deviation: 4h02m29s, median: 6m49s
    | smb2-security-mode: 
    |   3.1.1: 
    |_    Message signing enabled and required
    | smb2-time: 
    |   date: 2023-08-14T23:48:40
    |_  start_date: 2023-08-14T23:39:56
    | smb-security-mode: 
    |   account_used: <blank>
    |   authentication_level: user
    |   challenge_response: supported
    |_  message_signing: required
    | smb-os-discovery: 
    |   OS: Windows Server 2016 Standard 14393 (Windows Server 2016 Standard 6.3)
    |   Computer name: FOREST
    |   NetBIOS computer name: FOREST\x00
    |   Domain name: htb.local
    |   Forest name: htb.local
    |   FQDN: FOREST.htb.local
    |_  System time: 2023-08-14T16:48:37-07:00

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 38.53 seconds
