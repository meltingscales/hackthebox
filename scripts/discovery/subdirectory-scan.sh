#!/usr/bin/env bash

: ${1?" Error.
Usage: $0 <TARGET> [protocol] [output_dir].
You forgot to supply a TARGET"}

TARGET=$1
PROTOCOL=${2:-http} # optional args
OUTPUT_DIR=${3:-output}

echo "Writing to a series of files like '$TARGET.*.txt' in the directory '$OUTPUT_DIR'."
echo "You can view them live with 'tail -f FILE'."
echo "This might take a while, consider running this in a separate terminal."

if [[ ! -d $OUTPUT_DIR ]]; then
    mkdir -p $OUTPUT_DIR
fi

dirb $PROTOCOL://$TARGET    -o $OUTPUT_DIR/$TARGET.dirb.txt     >/dev/null 2>&1 & 

wfuzz --hc 404 -f $OUTPUT_DIR/$TARGET.wfuzz-directory-list-1.0.txt -w ~/Git/SecLists/Discovery/Web-Content/directory-list-1.0.txt $PROTOCOL://$TARGET/FUZZ    >/dev/null 2>&1 &

FAIL=0

for job in `jobs -p` #for all background processes,
do
echo "wait on job $job"
    wait $job || let "FAIL+=1" #wait for it to exit, or, if it exits non-zero, increment FAIL
done

if [ "$FAIL" == "0" ]; then
    echo "Done!"
else
    echo "Failed! ($FAIL jobs)"
    exit $FAIL
fi

exit 0
