import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


x = sp.symbols('x')


P = x**3 - 6*x**2 + 11*x - 6


raices = sp.solveset(P, x, domain=sp.Reals)


raices = [float(raiz) for raiz in raices]


P_func = sp.lambdify(x, P, 'numpy')


x_vals = np.linspace(-1, 4, 400)
y_vals = P_func(x_vals)


plt.plot(x_vals, y_vals, label=r'$P(x) = x^3 - 6x^2 + 11x - 6$', color='blue')


for raiz in raices:
    plt.scatter(raiz, 0, color='red', zorder=5)
    plt.text(raiz, 0.5, f'({raiz:.2f}, 0)', color='red', ha='center')


plt.xlabel('x')
plt.ylabel('P(x)')
plt.title('Gráfica de un polinomio y sus raíces')


plt.legend()


plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.grid(True)
plt.show()
