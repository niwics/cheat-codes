#!/bin/bash

# how to reload the .bashrc or .profile files (Linux + OS X)
#source ~/.profile

# conditions =====================
# if string is empty
if [ -z "$var" ] then
  echo "is empty"
else
  echo "not empty"
fi
# if directory exists
dirname=test
if [ ! -d ${dirname} ]; then
  echo "Dir ${dirname} does not exist!"
else
  echo "Dir ${dirname} exists!"
fi

# dates =====================
# yesterday
date -d "1 day ago" '+%Y-%m-%d'
date -d "12 hours ago" '+%Y-%m-%d'


# artihmetics =====================
COUNT=$(expr $FIRSTV - $SECONDV)
MYVAR_INCREMENTED=$(($MYVAR+1))

# strings
# OS X: cut the last char
echo "${myvar%?}"


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

# grep
# recursive - process all subdirectories
grep -R /some/path | grep "myfile"

# iterate over lines =====================
ls -l /my/path | while read line
do
  echo $line
done

# iterate by lines of file
input="/tmp/somefile"
while IFS= read -r line; do echo "${line}"; done < $input

# iterate over the array
MY_NUMBERS=( one two threee )
for var in "${MY_NUMBERS[@]}"
do
  echo "My number: ${var}"
done

# iterate with range
for day in {1..30};
do
  echo $day
  # zero padding
  day_pad=`printf "%02d" $day`
  echo "Day with zero padding: ${day_pad}"
done