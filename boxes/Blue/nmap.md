┌─[✗]─[user@parrot]─[~]
└──╼ $sudo nmap -sS -sV 10.10.10.40
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-01 19:19 UTC
Nmap scan report for 10.10.10.40
Host is up (0.041s latency).
Not shown: 991 closed tcp ports (reset)
PORT      STATE SERVICE      VERSION
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49155/tcp open  msrpc        Microsoft Windows RPC
49156/tcp open  msrpc        Microsoft Windows RPC
49157/tcp open  msrpc        Microsoft Windows RPC
Service Info: Host: HARIS-PC; OS: Windows; CPE: cpe:/o:microsoft:windows


┌─[user@parrot]─[~]
└──╼ $nmap -v -p 139,445 --script=smb-os-discovery.nse 10.10.10.40
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-01 19:36 UTC
NSE: Loaded 1 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 19:36
Completed NSE at 19:36, 0.00s elapsed
Initiating Ping Scan at 19:36
Scanning 10.10.10.40 [2 ports]
Completed Ping Scan at 19:36, 0.04s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 19:36
Completed Parallel DNS resolution of 1 host. at 19:36, 0.00s elapsed
Initiating Connect Scan at 19:36
Scanning 10.10.10.40 [2 ports]
Discovered open port 445/tcp on 10.10.10.40
Discovered open port 139/tcp on 10.10.10.40
Completed Connect Scan at 19:36, 0.04s elapsed (2 total ports)
NSE: Script scanning 10.10.10.40.
Initiating NSE at 19:36
Completed NSE at 19:36, 2.38s elapsed
Nmap scan report for 10.10.10.40
Host is up (0.038s latency).

PORT    STATE SERVICE
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Host script results:
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: haris-PC
|   NetBIOS computer name: HARIS-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2024-11-01T19:37:21+00:00

NSE: Script Post-scanning.
Initiating NSE at 19:36
Completed NSE at 19:36, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 2.69 seconds


┌─[✗]─[user@parrot]─[~]
└──╼ $nmap -p 445 -v --open --script smb-vuln* 10.10.10.40
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-01 19:31 UTC
NSE: Loaded 11 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 19:31
Completed NSE at 19:31, 0.00s elapsed
Initiating Ping Scan at 19:31
Scanning 10.10.10.40 [2 ports]
Completed Ping Scan at 19:31, 0.06s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 19:31
Completed Parallel DNS resolution of 1 host. at 19:31, 0.00s elapsed
Initiating Connect Scan at 19:31
Scanning 10.10.10.40 [1 port]
Discovered open port 445/tcp on 10.10.10.40
Completed Connect Scan at 19:31, 0.04s elapsed (1 total ports)
NSE: Script scanning 10.10.10.40.
Initiating NSE at 19:31
Completed NSE at 19:31, 12.71s elapsed
Nmap scan report for 10.10.10.40
Host is up (0.060s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-vuln-ms17-010: 
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|           
|     Disclosure date: 2017-03-14
|     References:
|       https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
|       https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
|_smb-vuln-ms10-061: NT_STATUS_OBJECT_NAME_NOT_FOUND
|_smb-vuln-ms10-054: false

NSE: Script Post-scanning.
Initiating NSE at 19:31
Completed NSE at 19:31, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 13.12 seconds


┌─[user@parrot]─[~]
└──╼ $nmap --script smb-enum-shares -p139,445 10.10.10.40
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-01 19:38 UTC
Nmap scan report for 10.10.10.40
Host is up (0.037s latency).

PORT    STATE SERVICE
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Host script results:
| smb-enum-shares: 
|   account_used: guest
|   \\10.10.10.40\ADMIN$: 
|     Type: STYPE_DISKTREE_HIDDEN
|     Comment: Remote Admin
|     Anonymous access: <none>
|     Current user access: <none>
|   \\10.10.10.40\C$: 
|     Type: STYPE_DISKTREE_HIDDEN
|     Comment: Default share
|     Anonymous access: <none>
|     Current user access: <none>
|   \\10.10.10.40\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: Remote IPC
|     Anonymous access: READ
|     Current user access: READ/WRITE
|   \\10.10.10.40\Share: 
|     Type: STYPE_DISKTREE
|     Comment: 
|     Anonymous access: <none>
|     Current user access: READ
|   \\10.10.10.40\Users: 
|     Type: STYPE_DISKTREE
|     Comment: 
|     Anonymous access: <none>
|_    Current user access: READ

Nmap done: 1 IP address (1 host up) scanned in 40.68 seconds
