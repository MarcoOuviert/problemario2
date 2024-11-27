import sympy as sp

x, y, z = sp.symbols('x y z')


ecuacion1 = sp.Eq(2*x - y + z, 5)
ecuacion2 = sp.Eq(3*x + 2*y - 4*z, 3)
ecuacion3 = sp.Eq(x + y + z, 6)


soluciones = sp.solve((ecuacion1, ecuacion2, ecuacion3), (x, y, z))


print("La solución del sistema es:")
for variable, valor in soluciones.items():
    print(f"{variable} = {valor}")
