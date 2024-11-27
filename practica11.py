import sympy as sp
x=sp.symbols("x")

funcion= x**2 + 3*x - 5
x0=2
derivada=sp.diff(funcion,x)
pendiente=derivada.evalf(subs={x:x0})
y0=funcion.evalf(subs={x:x0})
tangente= pendiente*(x-x0)+y0
print (f"la pendiente de la tangente en x= {x0} es: {pendiente}")
print(f"la escuacion de la recta tangente es: y= {sp.simplify(tangente)}")