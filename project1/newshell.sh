#!/bin/bash


PWDD=`pwd`
F='f'
DIRRD="`find $PWDD -mindepth 1 -maxdepth 2 -type d`"

for childdir in $DIRRD
do
  echo $childdir
done
