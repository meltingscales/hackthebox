    sudo nmap -sS -sC -sV -Pn 10.10.10.151

    Starting Nmap 7.92 ( https://nmap.org ) at 2023-08-15 09:20 BST
    Stats: 0:00:01 elapsed; 0 hosts completed (0 up), 0 undergoing Host Discovery
    Parallel DNS resolution of 1 host. Timing: About 0.00% done
    Nmap scan report for 10.10.10.151
    Host is up (0.10s latency).
    Not shown: 996 filtered tcp ports (no-response)
    PORT    STATE SERVICE       VERSION
    80/tcp  open  http          Microsoft IIS httpd 10.0
    | http-methods: 
    |_  Potentially risky methods: TRACE
    |_http-title: Sniper Co.
    |_http-server-header: Microsoft-IIS/10.0
    135/tcp open  msrpc         Microsoft Windows RPC
    139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
    445/tcp open  microsoft-ds?
    Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

    Host script results:
    | smb2-security-mode: 
    |   3.1.1: 
    |_    Message signing enabled but not required
    | smb2-time: 
    |   date: 2023-08-15T15:20:30
    |_  start_date: N/A
    |_clock-skew: 6h59m59s

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 67.77 seconds
