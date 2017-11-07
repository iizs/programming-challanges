#!/bin/bash

if [ z"$1" == 'z' ]; then
    echo Usage: $0 title
    exit
fi

if [ ! -d $1 ]; then
    echo "'$1' not found"
    exit
fi

BIN=
if [ -e $1/$1.py ]; then
    BIN="python $1/$1.py"
elif [ -e $1/$1.c ]; then
    gcc -Wall -o $1/$1.bin $1/$1.c || exit 1
    BIN="$1/$1.bin"
fi

if [ z"${BIN}" == 'z' ]; then
    echo "'$1' not implemented"
    exit
fi

if [ -e $1/$1.in ]; then
    if [ -e $1/$1.out ]; then
        ${BIN} < $1/$1.in > $1/$1.stdout || exit 1
        diff $1/$1.out $1/$1.stdout
    else
        ${BIN} < $1/$1.in || exit 1
    fi
else
    echo "'$1' has no inputfile"
    exit
fi

