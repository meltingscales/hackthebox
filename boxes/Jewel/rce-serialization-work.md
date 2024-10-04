We may have to create our own serialized payload to exploit CVE-2020-8165.

I tried to use https://github.com/hybryx/CVE-2020-8165 , and it seems to be able to `sleep` but not `curl` or use `/tcp` device file to connect to reverse shell.

I'm going to try to make my own serialized payload based off of this tutorial:

    https://0xdf.gitlab.io/2021/02/13/htb-jewel.html


See `./rails-console-dockerfile/start.sh`
