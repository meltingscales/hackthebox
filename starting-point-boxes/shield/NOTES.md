# Shield

## `nmap 10.10.10.29 -sV -sC`

    vagrant@vagrant-virtualbox ~> nmap 10.10.10.29 -sV -sC
    Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-02 12:30 CDT
    Nmap scan report for 10.10.10.29
    Host is up (0.031s latency).
    Not shown: 998 filtered ports
    PORT     STATE SERVICE VERSION
    80/tcp   open  http    Microsoft IIS httpd 10.0
    | http-methods: 
    |_  Potentially risky methods: TRACE
    |_http-server-header: Microsoft-IIS/10.0
    |_http-title: IIS Windows Server
    3306/tcp open  mysql   MySQL (unauthorized)
    Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 11.69 seconds

HTTP and MySQL.

## HTTP

Looks like IIS default page. Running `dirb`.

Apparently it runs wordpress??

- <http://10.10.10.29/wordpress/>
- <http://10.10.10.29/wordpress/wp-login.php?redirect_to=http%3A%2F%2F10.10.10.29%2Fwordpress%2Fwp-admin%2F&reauth=1>

### dirb results

- xmlrpc.php
- TODO put em here