from math import sqrt
for n in range(1, 60):
    r_org = 2.0
    r = r_org
    for i in range(n):
        r = sqrt(r)
    for i in range(n):
        r = r ** 2
    print ('With {} times sqrt and then {} times **2, the number {} becomes: {:.16f}'.format(n,n,r_org,r))


'''
The code square roots the double 2.0 n times and then exponents it n times

The reason the original value is altered after repetitions of the same forward
and reverse task is due to machine error. The computer can't record the value
to its full accuracy, and thus exponents back up an incorrect value.
'''
