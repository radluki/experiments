file="rand_milion.txt"
reg='0\.55.*444'
wc -l $file
echo "PYHTON:"
time cat $file | ./sed.py -r $reg -s "X==>" > p1
echo "SED:"
time cat $file | sed "s/$reg/X==>/g" > p2
echo "AWK:"
time cat $file | awk "{  gsub(/$reg/, \"X==>\", \$0); print \$0 }" > p3
if [ -z `diff p1 p2` ] && [ -z `diff p1 p3` ]
then
	echo PASS
else
	head p1 -n3
	echo -----------------------
	head p2 -n3
	echo -----------------------
	head p3 -n3
fi
./clean.sh
