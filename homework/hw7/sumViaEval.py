import sys

inputs = [eval(x) for x in sys.argv[1:]]
print('The sum of',end=' ')
for elmt in inputs:
   print(elmt,end=' ')

print('is',sum(inputs))
