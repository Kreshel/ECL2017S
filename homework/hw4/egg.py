from math import log, pi

M = 67
p = 1.038
c = 3.7
K = 0.0054

Tw = 100
Ty = 70
To = 4

t = ( M**(2/3) * c * p**(1/3) ) / ( K * pi**2 * (4*pi/3)**(2/3)) * log( 0.76 * (To-Tw)/(Ty-Tw) )

print(t)
