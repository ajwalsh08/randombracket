
# Import a random number generator.

import random

# Bring in the favorites and their chances of winning as a dictionary.

with open('chances.txt') as f:
	d = dict(line.strip().split(",") for line in f)

# Use random to determine an "outcome" for each game.

for team in d:
	outcome = random.randrange(1,100001)	
	chance = float(d[team]) * 1000
	if outcome < int(chance):
		print "Take the favorite: " + str(team) + " will WIN!"
	else:
		print "Ack! " + str(team) + " will LOSE!"