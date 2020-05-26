#!/usr/bin/env bash

if [ $# -lt 1 ]; then
    echo "usage: $0 .Xresources"
    exit 1
fi

awk -f generate-muttrc.awk <(cat $1 | python3 ./xres-to-muttcolors.py) ./template.muttrc
