n = int(input("Ingrese un numero"))

factores = []


divisor = 2


while n % divisor == 0:
    factores.append(divisor)
    n //= divisor


divisor = 3
while divisor * divisor <= n:
    while n % divisor == 0:
        factores.append(divisor)
        n //= divisor
    divisor += 2


if n > 1:
    factores.append(n)


print(f"Factores primos: {factores}")
