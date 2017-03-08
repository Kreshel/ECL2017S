from math import pi, exp, sqrt

mu = 0
sigma = 2
x = 1

fx = 1 / (sqrt(2 * pi) * sigma) * exp(-0.5 * ((x-mu)/sigma) ** 2)

print(fx)

