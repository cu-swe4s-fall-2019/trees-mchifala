rm -f rand.txt
rm -f sorted.txt

for i in `seq 1 10000`; do
    echo $RANDOM $RANDOM >> rand.txt
done

for i in `seq 1 10000`; do
    echo $RANDOM $RANDOM >> tmp.txt
done

sort -n tmp.txt > sorted.txt