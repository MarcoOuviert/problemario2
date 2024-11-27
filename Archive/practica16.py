import sympy as sp


def encontrar_raices(polinomio):
    x = sp.Symbol('x')

    raices = sp.solveset(polinomio, x, domain=sp.S.Reals)

    return list(raices)


x = sp.Symbol('x')
polinomio = x ** 3 - 6 * x ** 2 + 11 * x - 6

raices_reales = encontrar_raices(polinomio)

print(f"Polinomio: {polinomio}")
print(f"Raíces reales: {raices_reales}")
