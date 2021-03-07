#!/usr/bin/env bash

nmap -sS -A 10.10.10.28 > scan.txt
cat scan.txt

# sudo nmap -sS -A -Pn 10.10.14.1