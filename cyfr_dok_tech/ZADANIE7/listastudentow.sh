#!/bin/bash
FILE="daneStudenci.csv"

pliktex="studenci.tex"
plikpdf="studenci.pdf"

echo "\documentclass[12pt,a4paper]{article}"> $pliktex

echo "\usepackage[margin=2cm]{geometry}">> $pliktex
echo "\usepackage[utf8]{inputenc}">> $pliktex
echo "\usepackage{polski}">> $pliktex
echo "\usepackage{enumerate}">> $pliktex
echo "\usepackage{longtable}">> $pliktex
echo "\usepackage{array}">> $pliktex
echo "\begin{document}">> $pliktex

echo "\begin{center}">> $pliktex
echo "	{\large\textbf{Lista studentów}}">> $pliktex
echo "\end{center}">> $pliktex

echo "\renewcommand\arraystretch{1.5}">> $pliktex
echo "\begin{center}">> $pliktex
echo "	\setlength{\tabcolsep}{5pt}">> $pliktex
echo "	\begin{longtable}{|m{0.7cm}|m{2cm}|m{5cm}|b{3cm}|m{2cm}|m{3cm}|}\hline">> $pliktex
echo "		\textbf{L.p.} & \textbf{Katalog} & \textbf{Nazwisko i imię}& \textbf{Wydział} & {\raggedleft\textbf{Wiek}} &{\raggedleft\textbf{Płeć}} \\\\ \hline ">> $pliktex

echo "		\hline">> $pliktex
echo "		\endfirsthead">> $pliktex
echo "		\hline">> $pliktex
echo "		\textbf{L.p.} & \textbf{Katalog} & \textbf{Nazwisko i imię}& \textbf{Wydział} & {\raggedleft\textbf{Wiek}} &{\raggedleft\textbf{Płeć}} \\\\ \hline ">> $pliktex
echo "		\hline">> $pliktex
echo "		\endhead">> $pliktex
echo "		\endlastfoot">> $pliktex
while IFS=',' read -r lp katalog nazwisko imie wydzial wiek plec
do
    if [ $lp -gt 0 ]; then
        echo "		\centering $lp. &  $katalog &  $imie $nazwisko  & $wydzial & $wiek & $plec \\\\ \hline">> $pliktex
    fi
done < $FILE
echo "	\end{longtable}">> $pliktex
echo "\end{center}">> $pliktex
echo "\end{document}">> $pliktex
pdflatex $pliktex
pdflatex $pliktex
evince $plikpdf