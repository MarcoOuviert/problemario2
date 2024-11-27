import sympy as sp


M = sp.Matrix([[4, 2],
               [1, 3]])


autovalores = M.eigenvals()
autovectores = M.eigenvects()


print("Autovalores de la matriz:")
for valor, multiplicidad in autovalores.items():
    print(f"{valor} con multiplicidad {multiplicidad}")


print("\nAutovectores de la matriz:")
for valor, multiplicidad, vectores in autovectores:
    print(f"Autovalor: {valor}")
    for vector in vectores:
        print(f"Autovector: {vector}")
