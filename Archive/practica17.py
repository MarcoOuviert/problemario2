a = int(input("Ingrese un numero"))
b = int (input("Ingrese otro numero"))


suma_b = 0
suma_a = 0
for i in range(1, a // 2 + 1):
    if a % i == 0:
        suma_a += i


for i in range(1, b // 2 + 1):
    if b % i == 0:
        suma_b += i


if suma_a == b and suma_b == a:
    print(f"{a} y {b} son números amigables.")
else:
    print(f"{a} y {b} no son números amigables.")
