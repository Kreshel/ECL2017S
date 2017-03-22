# cannot use number as first character in variable
a1 = 2

# b is undefined
b = 2
a1 = b

# X should not be capitalized
x = 2
y = x + 4 # is it 6? yes

# Math should not be capitalized
from math import tan

# have to also import pi
from math import pi
print tan(pi)

# different quotation marks
pi = '3.14159’

# pi needs to be a float not a string
pi = 3.14159
print (tan(pi))

# one too many parenthesis
c = 4**3**2**3
_ = ((c-78564)/c + 32)

# conflicting data type; altered to just a float
discount = 0.12

# conflicting data type; altered to just an int
AMOUNT = 120

# conflicting data type; altered to just an int
amount = 120

# conflicting data type; altered to a string
address = 'hpl@simula.no'

# and is a reserved word
And = duck

# class is a reserved word, wrong quotation mark
Class = "INF1100, gr 2"

# x is not defined
x = 2
continue_ = x > 0

# first tests if rev and fox are the same and they are; then tests if this string is in Persian string and assigns it to variable name true
rev = fox = True
Persian = ['a human language']
true = fox is rev in Persian
