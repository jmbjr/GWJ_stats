import sys, json, collections

namesfile = sys.argv[1]
outfile = sys.argv[2]
unique_names = {}

with open(namesfile) as f:
	names = f.readlines()

for n in names:
	if unique_names.has_key(n):
		unique_names[n]+=1
	else:
		unique_names[n]=1

Dev = collections.namedtuple('Dev', 'entries name')

with open(outfile, 'a') as out:
#	json.dump(unique_names, out)
	sorted_list = sorted([Dev(v,k) for (k,v) in unique_names.items()],reverse = True) 
	i=0
	for s in sorted_list:
		person = sorted_list[i]
		out.write("{}\t{}\n".format(person.entries, person.name.rstrip()))
		i+=1
