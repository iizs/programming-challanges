#!/bin/bash

if [ z"$1" == 'z' ]; then
    echo Usage: $0 title
    exit
fi

DIRNAME="$1"
MODULE=`basename "$1"`

if [ ! -d ${DIRNAME} ]; then
    echo "'${DIRNAME}' not found"
    exit
fi

BIN=
if [ -e ${DIRNAME}/${MODULE}.py ]; then
    BIN="python ${DIRNAME}/${MODULE}.py"
elif [ -e ${DIRNAME}/${MODULE}.c ]; then
    gcc -Wall -o ${DIRNAME}/${MODULE}.bin ${DIRNAME}/${MODULE}.c || exit 1
    BIN="${DIRNAME}/${MODULE}.bin"
elif [ -e ${DIRNAME}/Main.java ]; then
    javac -Xlint ${DIRNAME}/Main.java
    BIN="java -classpath ${DIRNAME} Main"
fi

if [ z"${BIN}" == 'z' ]; then
    echo "'${DIRNAME}' not implemented"
    exit
fi

if [ -e ${DIRNAME}/${MODULE}.in ]; then
    if [ -e ${DIRNAME}/${MODULE}.out ]; then
        ${BIN} < ${DIRNAME}/${MODULE}.in > ${DIRNAME}/${MODULE}.stdout || exit 1
        diff ${DIRNAME}/${MODULE}.out ${DIRNAME}/${MODULE}.stdout
    else
        ${BIN} < ${DIRNAME}/${MODULE}.in || exit 1
    fi
else
    echo "'${DIRNAME}' has no inputfile"
    exit
fi

