According to the box desc, this box is vulnerable to LFI.

https://book.hacktricks.xyz/pentesting-web/file-inclusion

I'm fucking SLEEP DEPRIVED so I'm going to use the official box writeup to follow along.

Okay. Wow. It's a windows box, so of course `/etc/passwd` doesn't exist.

Try:

    http://10.10.10.151/blog/?lang=/windows/win.ini

It works. So. Apparently we now need to create a user, with a username whose name can be executed as code in PHP.