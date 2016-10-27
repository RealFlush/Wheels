
clear_wins = 0
non_clear_wins=0
from itertools import combinations
from random import shuffle
from random import randint
players = list(range(0,10))
games=[]
length=1000.0
combs = [x for x in combinations(players,2)]
for n in range(1,int(length)+1):
    wins=[0]*10
    shuffle(combs)
#    print(combs)
    for match in combs:
        wins[match[randint(0,1)]]+=1
#    print(wins)
    if max(wins) == 9:
        clear_wins+=1
    else:
        non_clear_wins+=1
    n+=1

print (str(round(non_clear_wins/length*100,4))+' %')
