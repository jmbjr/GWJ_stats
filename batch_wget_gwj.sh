#if arg 1 is blank, this will pull json files for all jams in ids.txt, then use some python magic to extract all contributors and sort them based on number of entries
# if arg 1 is NOT blank, it will just get a list of the winners (first result)

onlywinner=${1}
i=0;

if [ ! -z $onlywinner ];then
	names="winners.txt"
	unique="unique_winners.txt"
else
	names="names.txt"
	unique="unique_names.txt"
fi

rm $names
rm $unique

for id in `cat ids.txt`; 
do 
	((i=i+1));
	wget  https://itch.io/jam/${id}/results.json;
	mv results.json;  
	mv -f results.json "GWJ-${i}.json"; 
	python get_names.py "GWJ-${i}.json" ${names} ${onlywinner}
done

python get_unique_names.py ${names} ${unique}

