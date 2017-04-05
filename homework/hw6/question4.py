eps = 1.0
while 1.0 != 1.0 + eps:
    print ('...............', eps)
    eps /= 2.0
print ('final eps:', eps)


'''
The code runes a while loops as long as 1.0 is not equal to 1.0 plus value eps.
Eps is divided by 2 on every loop until the machine is no longer able to precisely
record eps as a non-zero value.

The loop thus breaks when 1.0 + eps = 1.0
'''
