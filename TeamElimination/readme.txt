The generatory.py python script on running generates a table standing of N teams, where N is taken from User Input. 

The table of wins, losses, games left to play, as well as which pairs of teams have how many games remaining to be played is generated randomly subject to some conditions. 

Based on these tables, for each of the N teams, one graph is generated, and if the maxflow for that graph is less than a particular value, that team is definitely eliminated.
This value is determined for each team's graph separately.
