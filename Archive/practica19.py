
N = int(input("Ingrese la dimension de la cuadricula"))


factorial_2N = 1
for i in range(1, 2 * N + 1):
    factorial_2N *= i

factorial_N = 1
for i in range(1, N + 1):
    factorial_N *= i


caminos = factorial_2N // (factorial_N * factorial_N)


print(f"El número de caminos en una cuadrícula {N}x{N} es: {caminos}")
