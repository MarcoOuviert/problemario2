import sympy as sp


def calcular_determinante(matriz):



    M = sp.Matrix(matriz)


    if M.shape[0] > 4 or M.shape[1] > 4:
        raise ValueError("La matriz no puede tener dimensiones mayores a 4x4.")


    return M.det()


# Ejemplo de uso
matriz_3x3 = [
    [2, 1, 3],
    [0, -1, 4],
    [1, 0, 5]
]

matriz_4x4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


print("Determinante de la matriz 3x3:", calcular_determinante(matriz_3x3))
print("Determinante de la matriz 4x4:", calcular_determinante(matriz_4x4))
