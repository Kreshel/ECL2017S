numbers = list(range(10))
print(numbers)

for n in numbers:
   i = len(numbers)//2
   del numbers[i]
   print ('n={}, del {}'.format(n,i), numbers)

'''
i is set to half the length of numbersrounded down. The next line deletes this
index in the list. However, since the length of numbers changes on every loop,
n is iterated in an undesirable way
'''
