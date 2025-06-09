import hashlib

email='753735754e377464@master.guild'

hashedemail=(str(hashlib.sha256(email.encode()).hexdigest()))

print("/changepasswd/"+hashedemail)