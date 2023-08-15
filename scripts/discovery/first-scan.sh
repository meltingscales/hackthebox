#!/usr/bin/env bash

: ${1?"Usage: $0 <target>. You forgot to supply a target"}

target=$1

nmap -sS -sC -sV -Pn $1