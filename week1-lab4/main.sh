#!/bin/bash
file=$1 #→ sample.txt
tr '[:upper:]' '[:lower:]' < "$file" |	#take input from file and lowercase m convert hnge
tr -cs '[:alnum:]' '\n' |		#squeeze repeated characters and goes to next line
sort |
uniq -c |
sort -nr | head


