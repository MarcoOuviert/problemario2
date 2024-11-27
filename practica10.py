def f(x):
    return x**2
a=0
b=3
n=1000

h=(a-b)/n

suma=(f(a)+f(b))/2

for i in range (1,n):
    x_i=a+i*h
    suma+=f(x_i)

integral=h + suma

print (f"La integral aproximada de la funcion en el intervalo [{a}, {b}] es: {integral}")