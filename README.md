example usage:

ensure ids.txt includes the list of all GWJ jam_id values.
(I got this list by viewing source for each GWJ results page the ctrl+f for jam_id)

to get list of ALL contributors, then sort by number of times they entered a GWJ jam, run:

./batch_wget_gwj.sh

creates new files: names.txt and unique_names.txt (files deleted and rewritten after each run)

to limit the lists to only the winners (assumed to be the first result in each json file) just add any string:

./batch_wget_gwj.sh winners

creates new files: winners.txt and unique_winners.txt


currently the script doesn't delete the json files each run and always pulls them again.  
