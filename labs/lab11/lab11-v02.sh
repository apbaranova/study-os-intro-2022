#!/bin/bash

gcc lab11-v2.c -o lab11-v2
./lab11-v2
code=$?
case $code in
    0) echo "Число меньше 0";;
    1) echo "Число больше 0";;
    2) echo "Число равно 0";;
esac
