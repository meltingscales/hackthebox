#!/usr/bin/env bash

payload="AAAAAAAAAAAAAAAAA"

while [ 1 ]; do


  echo -e $payload | nc 94.237.62.195 46344

  payload="$payload""A"
  echo $payload
#  sleep 1

done

