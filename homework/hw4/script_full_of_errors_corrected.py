a1 = 2                      # numbers can't start a variable
a1 = 3                      # undeclared variable b
x = 2
y = x + 4 # is it 6?        # undeclared variable X, changed to x
from math import tan        # had math capitalized
from math import pi         # had no pi import
print(tan(pi))              # no parenthesis around print
pi = "3.14159"              # not same quotations
print (tan(3.14159))        # cannot perform math functions on a string
c = 4**3**2**3
_ = ((c-78564)/c + 32)      # too many parenthesis
discount = .12              # character and int data conflict
AMOUNT = -120               # character and int data conflict
amount = 120                # character and int data conflict
address = 'hpl@simula.no'   # string data type requires quotations
And = 'duck'                # and is reserved word; string require quotations
Class = "INF1100, gr 2"     # wrong quotation; class is reserved word
continue_ = x > 0
rev = fox = True
Persian = ['a human language']
true = fox is rev in Persian # programs compares fox to rev and returns true; then searches if True is in Persian list and it's not
