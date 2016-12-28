#!/bin/bash


# dates =====================
# yesterday
date -d "1 day ago" '+%Y-%m-%d'
date -d "12 hours ago" '+%Y-%m-%d'


# artihmetics =====================
COUNT=$(expr $FIRSTV - $SECONDV)


# line filtering/skipping =====================
# get first three lines
head -3 myfile.txt
# get last three lines
tail -3 myfile.txt
# skip first three lines and get the rest
tail -n +4 myfile.txt

# string filtering =====================
# using sed with groups - do not forget to escape the parentheses!
echo "/test/my/path" | sed -e 's/.*\/\(.*\)$/\1/g'  # path
# filter some cols
echo "one two three" | cut -d " " -f 1,3  # one three (necessary to set the delimiter!)

# iterate over lines =====================
ls -l /my/path | while read line
do
  echo $line
done
