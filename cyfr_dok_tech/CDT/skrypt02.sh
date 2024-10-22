#!/bin/bash

pliktex="zadanie2.tex"
plikpdf="zadanie2.pdf"

echo "\documentclass{article}" > $pliktex
echo "\begin{document}" >> $pliktex
echo "hello" >> $pliktex
echo "\end{document}" >> $pliktex

pdflatex $pliktex
pdflatex $pliktex

evince $plikpdf
