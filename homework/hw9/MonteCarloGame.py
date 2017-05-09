#!/usr/bin/env python

import random
import matplotlib.pyplot as plt

plt.clf()

switchProb = []
noSwitchProb = []

switchWins = 0
ngames = 1000
times = 0
x = []

ax = plt.gca()  # generate a plot handle
ax.set_xlabel('Trials') # set X axis title
ax.set_ylabel('Win Percentage')  # set Y axis title
ax.axis([0, ngames, 0, 100]) # set axix limits [xmin, xmax, ymin, ymax]
plt.hold('on')  # add all data files to the same plot
    
for i in range(ngames):
    prize = random.randint(1,3)
    guess = random.randint(1,3)
    view = guess
    while view == prize or view == guess:
        view = random.randint(1,3)
    newGuess = view
    while newGuess == guess or newGuess == view:
        newGuess = random.randint(1,3)

    if newGuess == prize:
        switchWins += 1
        
    times += 1
    x.append(times)
        
    
    switchPercentage = 100*(switchWins / times)
    noSwitchPercentage = 100 - switchPercentage
    
    switchProb.append(switchPercentage)
    noSwitchProb.append(noSwitchPercentage)
    #plt.plot([times], [switchPercentage], 'ro')
    #plt.plot([times], [noSwitchPercentage], 'bo')# [x], [y]
    
plt.plot(x,switchProb,'c--')
plt.plot(x,noSwitchProb,'b-')
plt.legend(['Switch','No Switch'])
plt.savefig('MonteCarloGame.png')
