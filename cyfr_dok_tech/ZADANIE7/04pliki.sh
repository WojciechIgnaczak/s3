#!/bin/bash
FILE="dane2.txt"
while IFS="," read -r imienazwisko szkola panpani
do
echo "$i. $imienazwisko $szkola"
i=$(($i+1))
done < $FILE