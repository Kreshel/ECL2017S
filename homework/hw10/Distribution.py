import random
import matplotlib.pyplot as plt
import numpy as np

    
def f(x):
    return (x+1)/12 * np.exp(-(x-1)**2/(2*x))

def graph():
    #x = np.array(15)
    x = np.linspace(0.000000001,15,100)
    y = f(x)
    
    plt.plot(x,y)
    plt.legend(['f(x)'])
    plt.show()

def histogram():
    numbers = []
    for i in range(10000):
        base = random.uniform(0, 15)
        height = random.uniform(0, 0.2)
    
        if height < f(base):
            numbers.append(base)
            
    x = np.linspace(0.000000001,15,100)
    y = f(x)
    
    plt.plot(x,y,'r-')
    plt.legend(['f(x)'])
    plt.hold('on')
    num_bins = 30
    n, bins, patches = plt.hist(numbers, num_bins, normed=1, facecolor='blue', alpha=0.5)
    plt.show()
    
def points():
    plt.hold('on')
    
    for i in range(5000):
        base = random.uniform(0, 15)
        height = random.uniform(0, 0.2)
        
        if height < f(base):
            plt.plot([base],[height],'r.')
        else:
            plt.plot([base],[height],'k.')
            
    plt.show()
            
        
graph()
histogram()
points()
