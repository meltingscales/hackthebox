Looks like 10.10.11.219 has port 22 and port 80 open.

And we need to add `pilgrimage.htb` to `/etc/hosts`.

Looks like it's a web form that lets you upload files.

Going to try to execute PHP code.

I don't think the login form is SQL injectable. I feel like I have to do something with the file upload.

Well, from `dirb`, looks like they have an exposed `.git/` directory:

    curl http://pilgrimage.htb/.git/

Gonna read <https://infosecwriteups.com/exposed-git-directory-exploitation-3e30481e8d75> and use `GitDumper` from <https://github.com/internetwache/GitTools>.

See `./pilgrimageDumped` for git repo.

Apparently there's a committer whose email is `emily@pilgrimage.htb`.

Maybe we can login as `emily@pilgrimage.htb` or `emily`.

They sadly use prepared statements, so SQLi won't work.

Perhaps there's a vulnerability in the "Bulletproof" image upload library.

...

After reviewing `index.php`, I think I can execute command injection.

```php
      exec("/var/www/pilgrimage.htb/magick convert /var/www/pilgrimage.htb/tmp/" . $upload->getName() . $mime . " -resize 50% /var/www/pilgrimage.htb/shrunk/" . $newname . $mime);
```

If I can name a file `| sleep 10;.jpeg`, I might be able to verify this.