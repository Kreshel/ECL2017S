#!/usr/bin/env python

import platform

my_string = 'Python is the best language for String Manipulation!'

print("""This is Python version {}

{}

{}

!otlpnmgnit o gunlte h inhy

pYTHON IS THE BEST LANGUAGE FOR sTRING MANIPULATION!


The sentence 'Python is the best language for String manipulation!' contains
4 'a' letters, and
0 'A' letters!

Python\nis\nthe\nbest\nlanguage\nfor\nString\nmanipulation!

PYTHON\nIS\nTHE\nBEST\nLANGUAGE\nFOR\nSTRING\nMANIPULATION!
""".format(platform.python_version(), my_string, my_string[::-1]))
