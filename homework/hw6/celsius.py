Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
print('     C     F')
'''
for C in Cdegrees:
   F = (9.0/5)*C + 32
print('%5d %5.1f' % (C,F))
'''
i = 0
while i<13:
   F = (9.0/5)*Cdegrees[i] + 32
   print('%5d %5.1f' % (Cdegrees[i],F))
   i += 1
