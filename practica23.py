import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 400)
onda1 = np.sin(x)
onda2 = np.cos(x)
superposicion = onda1 + onda2

plt.plot(x, onda1, label='Onda 1 (sin(x))', color='blue')
plt.plot(x, onda2, label='Onda 2 (cos(x))', color='red')
plt.plot(x, superposicion, label='Superposición', color='green', linestyle='--')

plt.xlabel('x')
plt.ylabel('Amplitud')
plt.title('Superposición de Dos Ondas')
plt.legend()
plt.grid(True)
plt.show()
