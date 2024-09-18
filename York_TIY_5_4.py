import random as r

alien_color = ["green", 'yellow', 'red']

if alien_color[r.randint(0,2)] == 'green':
    print("Player earned 5 points!")
else:
    print("Player earned 10 points!")