rm -f rand.txt
rm -f sorted.txt
rm -f test.txt

for i in `seq 1 10000`; do
    echo $RANDOM $RANDOM >> tmp1.txt
done

for i in `seq 1 10000`; do
    echo $RANDOM $RANDOM >> tmp2.txt
done

for i in `seq 1 10`; do
    echo $i $i >> test.txt
done

sort -u tmp1.txt > rand.txt

sort -n -u tmp2.txt > sorted.txt