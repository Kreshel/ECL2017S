import numpy as np

# our model parameters are most likely correct if distance is minimized
T = [10,12,14,15,16,18,20]

def N(t,a,b,c):
    global T
    i = T.index(t)
    #print(i,np.sum(cells[:,:,:,i]))
    return a * np.exp(-b * np.exp(-c*np.sum(cells[:,:,:,i])))

# returns probability
def prob(ti,a,b,c,sigma):
    global T
    i = T.index(ti)
    
    return 1 / (sigma*np.sqrt(2*np.pi)) * np.exp(- (np.sum(cells[:,:,:,i])-N(ti,a,b,c))**2 / (2*sigma**2))


def likelihood(a,b,c,sigma):
    overallProb = 0
    global T
    for i in range(7):
        overallProb *= prob(T[i],a,b,c,sigma)
        
    return overallProb


# returns sum over log of probabilities
def logLikelihood(a,b,c,sigma):
    overallProb = 0
    global T
    for i in range(7):
        overallProb += np.log10(prob(T[i],a,b,c,sigma))
        
    return overallProb
