#! /bin/bash


# input PJ Name
read -p "Please input PJ name:" PJname
echo $PJname >> ./rst.txt
PWDD=`pwd`
cd $PWDD
cd ./project
F='f'

DIRRD="`find $PWDD -type d`"
for file in $(ls ./)
do
  echo "Judging: [$file]:"
  echo ""
  id=${file:0:11}
  newName="$id.py"
  mv $file $newName
  python $newName
	read -p "Please judge: " input_char
	if [ $input_char = $F ]
  # wrong
	then
		read -p 'Please input some remarks:' remark
		info="$id : $remark"
		echo $info >> ../rst.txt
	fi
done