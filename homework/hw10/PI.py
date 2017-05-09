import random
import math
import matplotlib.pyplot as plt

def computePI(numThrows):
    # initialize number inside and total count to 0
    ins = 0
    count = 0
    piVal = []

    # loop to test numThrows number of random throws
    for i in range(1, numThrows+1):
        # throw dart in random location inside square of side length 2
        xPos = random.uniform(-1.0, 1.0)
        yPos = random.uniform(-1.0, 1.0)
        # test if dart is inside circle of radius 1
        if math.hypot(xPos, yPos) < 1:
            ins += 1
        count += 1
        
        piVal.append(4 * (ins / count))
    # returns value of pi
    
    return piVal

def graphPi(piVals,numThrows):
    throws = []
    for i in range(numThrows):
        throws.append(i+1)
        
    plt.clf()
    plt.plot(throws,piVals)
    plt.xlabel('Number of Simulated Points')
    plt.ylabel('Approximation Value of Pi')
    plt.xscale('log')
    plt.axis([0, numThrows, 2, 4]) # [xmin, xmax, ymin, ymax]
    plt.title('Estimating Pi by Monte Carlo Simulation')
    plt.savefig('Pi.png')
    plt.show()

    
num = 100000
graphPi(computePI(num),num)
