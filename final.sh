#!/bin/bash

clear

pocketsphinx_continuous -infile lecture.wav > transcript.txt

python sum.py

python wc.py

./htmlpage.sh > page.html
cat summary.txt >> page.html
./htmlpage2.sh >> page.html
