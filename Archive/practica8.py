import sympy as pn
from sympy import pprint
h=1e-5

def f(x):
    return 3*x**2+2*x

x=2.0
derivada=(f(x+h)-f(x-h))/(2*h)

pprint(derivada)