echo PYTHON
filename="rand_milion.txt"
reg="0\.55.*44"
wc $filename -l
time ./grep.py -f $filename -r $reg > g1
echo GREP
time grep "$reg" $filename > g2
if [ -z `diff g1 g2` ]
then
	echo PASS
else
	head g1
	echo ----------------------------
	head g2
fi
./clean.sh
