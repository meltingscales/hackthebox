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
    