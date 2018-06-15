#!/bin/bash

if [ z"$1" == 'z' ]; then
    echo Usage: $0 title
    exit
fi

MODULE=`basename "$1"`

if [ ! -d ${MODULE} ]; then
    echo "'${MODULE}' not found"
    exit
fi

BIN=
if [ -e ${MODULE}/${MODULE}.py ]; then
    BIN="python ${MODULE}/${MODULE}.py"
elif [ -e ${MODULE}/${MODULE}.c ]; then
    gcc -Wall -o ${MODULE}/${MODULE}.bin ${MODULE}/${MODULE}.c || exit 1
    BIN="${MODULE}/${MODULE}.bin"
elif [ -e ${MODULE}/Main.java ]; then
    javac ${MODULE}/Main.java
    BIN="java -classpath ${MODULE} Main"
fi

if [ z"${BIN}" == 'z' ]; then
    echo "'${MODULE}' not implemented"
    exit
fi

if [ -e ${MODULE}/${MODULE}.in ]; then
    if [ -e ${MODULE}/${MODULE}.out ]; then
        ${BIN} < ${MODULE}/${MODULE}.in > ${MODULE}/${MODULE}.stdout || exit 1
        diff ${MODULE}/${MODULE}.out ${MODULE}/${MODULE}.stdout
    else
        ${BIN} < ${MODULE}/${MODULE}.in || exit 1
    fi
else
    echo "'${MODULE}' has no inputfile"
    exit
fi

