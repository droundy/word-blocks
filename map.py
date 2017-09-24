import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

import scipy.interpolate as interpolate
from scipy import misc

mymap=mpimg.imread('equirectangular.jpg')

plt.imshow(mymap)

print mymap.shape

theta = np.linspace(0,np.pi, mymap.shape[1])
phi = np.linspace(0,np.pi, mymap.shape[0])

THETA,PHI = np.meshgrid(theta,phi)

print THETA.shape, mymap[:,:,0].shape

#red = interp2d(THETA, PHI, mymap[:,:,0])
print THETA
#red = interpolate.RectBivariateSpline(THETA, PHI, THETA**2) # mymap[:,:,0])
#green = interp2d(THETA, PHI, mymap[:,:,1])
#blue = interp2d(THETA, PHI, mymap[:,:,2])

print('created red etc')

phi0 = .53

northpole = np.zeros((1000,1000,3))
x = np.linspace(-1.0,1, 1000)
y = np.linspace(-1.0,1, 1000)
X,Y = np.meshgrid(x,y)
S = np.sqrt(X**2+Y**2)
TH = np.arccos(1/(np.sqrt(1 + X**2 + Y**2)))
PH = np.arctan2(X,Y)

print northpole.shape
print mymap.shape[0]
for i in range(northpole.shape[0]):
    for j in range(northpole.shape[1]):
        ii = int(TH[i,j]*mymap.shape[0]/np.pi)
        jj = int((PH[i,j]+phi0)*mymap.shape[1]/(2*np.pi)) % mymap.shape[1]
        northpole[i,j,:] = mymap[ii,jj,:]

plt.figure()
plt.imshow(northpole)

misc.imsave('northpole.png', northpole)

southpole = np.zeros((1000,1000,3))
x = np.linspace(-1.0,1, 1000)
y = -np.linspace(-1.0,1, 1000)
X,Y = np.meshgrid(x,y)
S = np.sqrt(X**2+Y**2)
TH = np.arccos(-1/(np.sqrt(1 + X**2 + Y**2)))
PH = np.arctan2(X,Y)

print southpole.shape
print mymap.shape[0]
for i in range(southpole.shape[0]):
    for j in range(southpole.shape[1]):
        ii = int(TH[i,j]*mymap.shape[0]/np.pi)
        jj = int((PH[i,j]+phi0)*mymap.shape[1]/(2*np.pi)) % mymap.shape[1]
        southpole[i,j,:] = mymap[ii,jj,:]

plt.figure()
plt.imshow(southpole)

misc.imsave('southpole.png', southpole)

for side in range(4):
    uspole = np.zeros((1000,1000,3))
    x = -np.linspace(-1.0,1, 1000)
    z = -np.linspace(-1.0,1, 1000)
    X,Z = np.meshgrid(x,z)
    TH = np.arccos(Z/(np.sqrt(1 + X**2 + Z**2)))
    PH = np.arctan2(X,-1)

    print uspole.shape
    print mymap.shape[0]
    for i in range(uspole.shape[0]):
        for j in range(uspole.shape[1]):
            ii = int(TH[i,j]*mymap.shape[0]/np.pi)
            jj = int((PH[i,j]+phi0+side*np.pi/2)*mymap.shape[1]/(2*np.pi)) % mymap.shape[1]
            uspole[i,j,:] = mymap[ii,jj,:]

    plt.figure()
    plt.imshow(uspole)

    misc.imsave('side%d.png' % side, uspole)

#plt.show()
