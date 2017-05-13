import matplotlib.pyplot as plt
import numpy as np

T = [10,12,14,15,16,18,20]
Tvals = []

for i in range(len(T)):
    Tvals.append(np.sum(cells[:,:,:,i]))
    
plt.plot(T,Tvals,'bo-')
plt.title('Rat W09. No radiation Treatment.',fontweight='bold')
plt.ylabel('Tumor Cell Count')
plt.xlabel('Time [days]')
plt.minorticks_on()
plt.savefig('./results/LineGraph.png')
plt.show()
