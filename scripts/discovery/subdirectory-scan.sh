#!/usr/bin/env bash

: ${1?" Error.
Usage: $0 <target> [protocol=http].
You forgot to supply a target"}

target=$1
PROTOCOL=${2:-http} #optional arg

echo "Writing to a series of files like '$target.*' in the current directory."
echo "You can view them live with 'tail -f FILE'."

dirb $PROTOCOL://$target    -o $target.dirb.txt     >/dev/null 2>&1 & 
dirb $PROTOCOL://localhost  -o localhost.dirb.txt   >/dev/null 2>&1 &

FAIL=0

for job in `jobs -p` #for all background processes,
do
echo "wait on job $job"
    wait $job || let "FAIL+=1"
done

if [ "$FAIL" == "0" ];
then
    echo "Done!"
else
    echo "Failed! ($FAIL jobs)"
    exit $FAIL
fi

exit 0
