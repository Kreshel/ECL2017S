# A
a = 5
b = a
print (id(a), id(b))        # b points to a so they have the same address
 
c = b                       # c points to b so they have the same address
b = 3                       
print (a,b,c)               # a has value 5; b of 3; c of 5
print (id(a),id(b),id(c))   # c points to b so they have the same address
                            # b is assigned a new value so new address
 
b = a
b = 5
print (id(a), id(b))        # b points to a again so they have same address


# B
a = [5]
b = a
print (id(a), id(b))        # b points to a so they have the same address
 
b.append(1)
print (a,b)                 # lists are mutable so b changes a's value
print (id(a),id(b))         # lists are mutable thus changing a value does not introduce a new address


# C
a = [5]
b = list(a)
print (a,b)                 # b is a copy of a so same values
print (id(a), id(b))        # since it's a copy not alias, different address
 
b = a[:]
print (a,b)                 # same thing; b is just a copy
print (id(a), id(b))        # since it's a copy not alias, different address


# D

a = (5,)
b = tuple(a)
print (id(a), id(b))        # immutable data type so same address
 
b = a[:]
print (id(a), id(b))        # immutable data type so same address
