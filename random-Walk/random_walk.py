#random walk
#what'd be the longest random walk you can take so that on avg you'll end up 4 blocks or fewer from home

import random

def random_walk(n):
    """Return coordinates after 'n' block random walk"""
    x = 0
    y = 0

    for i in range(n):
        step = random.choice(['S', 'N', 'E', 'W'])
        if step == 'S':
            y = y - 1
        elif step == 'N':
            y = y + 1
        elif step == 'E':
            x = x + 1
        else:
            x = x - 1
    return (x,y)

for i in range(12):
    walk = random_walk(8)
    print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))
    