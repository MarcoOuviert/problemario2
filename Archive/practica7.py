import sympy as sp
from sympy import pprint

x= sp.symbols("x")

funcion_str=3*x**2+2*x

derivada=sp.diff(funcion_str,x)



print("La derivada de: ")
pprint(funcion_str)
print("Es:")
pprint(derivada)