import sys, json

jsonfile = sys.argv[1]
outfile = sys.argv[2]
onlywinner = False if len(sys.argv)==3 else True

with open(jsonfile) as f:
	results_json = json.load(f)['results']

with open(outfile, 'a') as out:
	for r in results_json:
		for c in r['contributors']:
			n=c['name'].encode('ascii','replace')
			print(n)
			out.write(n)
			out.write("\n")
		if onlywinner:
			break

