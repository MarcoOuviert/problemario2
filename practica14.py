import sympy as sp


A = sp.SparseMatrix(3, 3, {
    (0, 0): 1,
    (0, 2): 2,
    (1, 1): 3
})


B = sp.SparseMatrix(3, 3, {
    (0, 1): 4,
    (2, 0): 5,
    (2, 2): 6
})


C = A * B

print("Matriz A (dispersa):")
sp.pprint(A)

print("\nMatriz B (dispersa):")
sp.pprint(B)

print("\nMatriz resultante C = A * B (dispersa):")
sp.pprint(C)
