#!/bin/bash




# input file path
read -p "Please input file path:" filePath

# input PJ Name
read -p "Please input PJ name:" PJname
separator_line=' '
echo $separator_line >> $filePath
echo $PJname >> $filePath
echo $separator_line >> $filePath


PWDD=`pwd`
F='f'
DIRRD="`find $PWDD -mindepth 3 -maxdepth 3 -type d`"
for childdir in $DIRRD
do
	echo $childdir
        cd $childdir
#        cp ../../../treasure.txt ./treasure.txt # cp resource to local path for py script
       	python3 *.py
	read -p "Please judge: " input_char
	if [ $input_char = $F ]
	then
		echo $childdir
		read -p 'Please input some remarks:' remark
		id=$childdir
		id=${id%/*}
		id=${id##*/}
		info="$id : $remark"
		echo $info >> $PWDD/$filePath
	fi
done

echo $PWDD
cd $PWDD
 
echo 'ojbk'


