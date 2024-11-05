#!/bin/bash
mkdir ZADANIE3
echo −n "Podaj nazwe pliku(5 malych liter): "
read nazwa # wczytywanie z terminala do zmiennej liczba
if [[ "$nazwa" =~ ^[a-z]{5}$ ]]; then
    cd ZADANIE3
    touch $nazwa
    dzien=`date`
    echo $dzien >> $nazwa
    cal 9 1956 >> $nazwa
    echo ${dzien} >> ${nazwa}
    cd ..
else
    exit 1
fi
