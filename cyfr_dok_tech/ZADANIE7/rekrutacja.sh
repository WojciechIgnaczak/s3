#!/bin/bash

FILE="daneStudenci.csv"

    pliktex="pierwszy.tex"
    plikpdf="pierwszy.pdf"

echo " \documentclass[12pt,a4paper]{article}" > $pliktex
echo "\usepackage[margin=2cm]{geometry} " >>$pliktex
echo "\usepackage[utf8]{inputenc} " >>$pliktex
echo "\usepackage{polski} " >>$pliktex
echo "\usepackage{enumerate} " >>$pliktex

echo "\begin{document} " >>$pliktex
echo " \documentclass[12pt,a4paper]{article}" > $pliktex
echo "\usepackage[margin=2cm]{geometry} " >>$pliktex
echo "\usepackage[utf8]{inputenc} " >>$pliktex
echo "\usepackage{polski} " >>$pliktex
echo "\usepackage{enumerate} " >>$pliktex

echo "\begin{document} " >>$pliktex


while IFS=',' read -r lp katalog nazwisko imie wydzial wiek plec
do
    #echo "Lp. $lp, Katalog: $katalog, Nazwisko: $nazwisko, Imie: $imie, Wydział: $wydzial, Wiek: $wiek, płeć: $plec"
    if [ $lp -gt 0 ]; then
        echo "\hfill Płock, 19 listopada 2024 r. \\\\" >>$pliktex

        echo "\noindent" >>$pliktex
        if [[ $plec == "M" ]]; then
            echo "Szanowny Pan \\\\" >>$pliktex
        elif [[ $plec == "K" ]]; then
            echo "Szanowna Pani \\\\" >>$pliktex
        fi

        echo "$imie $nazwisko \\\\" >>$pliktex
        echo "wiek: $wiek" >>$pliktex
        echo "\bigskip" >>$pliktex

        echo "\begin{center}" >>$pliktex
        echo "    {\Large\textbf{Zawiadomienie}}" >>$pliktex
        echo "\end{center}" >>$pliktex

        echo "\bigskip " >>$pliktex

        if [[ $plec == "M" ]]; then
            echo "Z radością chcielibyśmy poinformować Pana, że w wyniku procesu rekrutacyjnego" >>$pliktex
            echo "\begin{center}" >>$pliktex
            echo "\textsf{\textbf{został Pan przyjęty}}" >>$pliktex
            echo "\end{center}" >>$pliktex
        elif [[ $plec == "K" ]]; then
            echo "Z radością chcielibyśmy poinformować Panią, że w wyniku procesu rekrutacyjnego" >>$pliktex
            echo "\begin{center}" >>$pliktex
            echo "\textsf{\textbf{została Pani przyjęta}}" >>$pliktex
            echo "\end{center}" >>$pliktex
        fi

        echo "na Wydział $wydzial z identyfikatorem \verb|$katalog|. " >>$pliktex
        echo "\vspace{2cm}" >>$pliktex

        echo "\noindent" >>$pliktex
        echo "Z poważaniem, \\\\" >>$pliktex
        echo "Dziekan" >>$pliktex
        echo "Wydziału $wydzial" >>$pliktex

        echo "\newpage" >>$pliktex
    fi
done < $FILE
echo "\end{document}" >>$pliktex

pdflatex $pliktex
pdflatex $pliktex
evince $plikpdf