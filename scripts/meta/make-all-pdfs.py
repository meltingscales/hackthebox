#!/usr/bin/env python3

import os
from pprint import pprint

# box paths
box_paths = ['boxes', 'starting-point-boxes']
box_paths = [os.path.abspath(p) for p in box_paths]

# file patterns
file_patterns = ["WRITEUP.md"]

if os.path.abspath('.').split('/')[-1] != 'hackthebox':
    print("Your working directory must be 'hackthebox'.")
    exit(1)

# pprint(box_paths)

# all glob patterns
glob_paths = []

for bp in box_paths:
    for fp in file_patterns:
        glob_paths.append(bp+"/**/"+fp)

pprint(glob_paths)

for rootdir in glob_paths:
    
    print(f"Processing '{rootdir}'...")

    # TODO

    for subdir, dirs, files in os.walk(rootdir):

        print(subdir, dirs, files)

        for file in files:
            print(os.path.join(subdir, file))
