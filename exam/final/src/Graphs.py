import matplotlib.pyplot as plt
import numpy as np

plt.clf()

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

plt.show()
