#!/usr/bin/env python

import sys

g = 9.81

try:
   v0 = float(sys.argv[1])
   t = float(sys.argv[2])
except IndexError:
   # raise IndexError('Both v0 and t must be supplied on the command line')
   print('Both v0 and t must be supplied on the command line')
   v0 = eval(input('v = ?\n'))
   t = eval(input('t = ?\n'))

try:
   if t < 0 or t > (2*v0/g):
      raise ValueError
   y = v0*t - 0.5*g*t**2
   print('y =',y)
except ValueError:
   print('t =', t,'is a non-physical value.')
   print('must be between 0 and 2v0/g =',2*v0/g)
