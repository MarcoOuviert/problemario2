import matplotlib.pyplot as plt

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

N = 10


fib_series = fibonacci(N)

acumulado = [sum(fib_series[:i+1]) for i in range(N)]

# Graficar
plt.bar(range(N), acumulado, color='skyblue')


plt.xlabel('Índice')
plt.ylabel('Suma acumulada')
plt.title('Gráfica de Fibonacci Acumulativo')


plt.show()
