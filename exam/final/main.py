# didn't know how to open folder to read python files
#  so I listed all the code in one comprehensive file..
#
#
#
#

import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt

##### Read Data In #####
matData = sio.loadmat('./data/cells.mat') # cells(y,x,z,time)

cells = np.array(matData['cells'])

plt.clf()
########################


##### Display Plots #####
T = [10,12,14,15,16,18,20]

for i in range(len(T)):
    fig = plt.figure(figsize=(25,25))
    fig.suptitle('Time = '+str(T[i])+' days. Brain MRI slices along Z-direction, Rat W09. No radiation treatment.',fontsize=20,fontweight='bold')
    fig.text(0.5, 0.04, 'Voxel Number in X-Direction', ha='center', va='center',fontsize='20')
    fig.text(0.06, 0.5, 'Voxel Number in y-Direction', ha='center', va='center', rotation='vertical',fontsize='20')
    for j in range(16):
        ax = plt.subplot(4,4,j+1)
        im = ax.imshow(cells[:,:,j,i],vmin=0,vmax=40000)
        ax.set_title('z ='+str(j+1),fontsize=20)
        ax.axis([0, 60, 40, 0]) # [xmin, xmax, ymin, ymax]
        fig.colorbar(im)
    plt.savefig('./results/Day'+str(T[i])+'.png')

#plt.show()
########################


##### Display Line Chart #####
Tvals = []
plt.clf()

for i in range(len(T)):
    Tvals.append(np.sum(cells[:,:,:,i]))
    
plt.plot(T,Tvals,'bo-')
plt.title('Rat W09. No radiation Treatment.',fontweight='bold',fontsize='20')
plt.ylabel('Tumor Cell Count',fontsize='20')
plt.xlabel('Time [days]',fontsize='20')
plt.minorticks_on()
plt.savefig('./results/LineGraph.png')
#plt.show()

########################


##### Probability Functions #####
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


a,b,c,sigma = (input('\nPlease input an a, b, c, and sigma for testing purposes (seperated by spaces): ').split())
a,b,c,sigma = eval(a), eval(b), eval(c), eval(sigma)
print('Log Likelihood =',logLikelihood(a,b,c,sigma),'with these parameters.\n')
########################
