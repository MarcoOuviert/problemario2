from sympy import pprint

a=3
b=-12
c=5

x_vertice=-b/(2*a)
f_vertice=a * x_vertice**2 + b * x_vertice + c

if a>0:
    print(f"El minimo de la funcion: ")
    pprint(f_vertice)
    print("en x= ")
    pprint(x_vertice)
else:
    print(f"El maximo de la funcion: ")
    pprint(f_vertice)
    print("en x= ")
    pprint(x_vertice)
