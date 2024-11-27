import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


x = sp.symbols('x')


f = sp.sin(x)


f_prime = sp.diff(f, x)


x0 = np.pi / 4


f_x0 = float(f.subs(x, x0))
f_prime_x0 = float(f_prime.subs(x, x0))


def tangente(x_val):
    return f_prime_x0 * (x_val - x0) + f_x0


x_vals = np.linspace(0, 2 * np.pi, 400)
y_vals = np.sin(x_vals)


plt.plot(x_vals, y_vals, label="f(x) = sin(x)", color='blue')


y_tangente_vals = tangente(x_vals)
plt.plot(x_vals, y_tangente_vals, label="Recta tangente en x = π/4", color='red', linestyle='--')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Función y su Recta Tangente')


plt.scatter([x0], [f_x0], color='green', zorder=5)
plt.text(x0 + 0.2, f_x0, f'({x0:.2f}, {f_x0:.2f})', color='green')


plt.legend()

plt.grid(True)
plt.show()
