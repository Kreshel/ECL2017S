def diff2nd(func, x, h=1E-6):
    r = (func(x-h) - 2*func(x) + func(x+h))/float(h*h)
    return r

g = lambda x: x**2 + 4*x + 1

x = 2
diff2nd_g = diff2nd(g, x)
print ( "g’’(x=%f)=%f" % (x, diff2nd_g) )
