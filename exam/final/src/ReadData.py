import numpy as np
import scipy.io as sio

matData = sio.loadmat('./data/cells.mat') # cells(y,x,z,time)

cells = np.array(matData['cells'])
