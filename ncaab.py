
# Import a random number generator.

import random

# Bring in the favorites and their chances of winning as a dictionary.

with open('chances.txt') as f:
	favorites = dict(line.strip().split(",") for line in f)

# Create a function that chooses winners using random numbers generation.

def losers(d):
	lst = list() 
	for team in d:
		outcome = random.randrange(1,100001)	
		chance = float(d[team]) * 1000
		if outcome < int(chance):
			pass
		else:
			lst.append(str(team))
	return lst

# Ask the user how many upsets they think will happen. 

upsets = raw_input("How many upsets do you think will happen?")

# Run the function once.

picks = losers(favorites)

# Check its length. If it returns more than 5 teams, run it again. Else, print it.

while len(picks) != int(upsets):
	picks = losers(favorites)
else: 
	print picks