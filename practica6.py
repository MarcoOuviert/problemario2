a=0
b=1
c=0
suma=0
num=int(input("Cuantos numeros quieres sumar?"))
for i in range (num):
    c=a+b
    a=b
    b=c
    suma=suma+c
    print (c)
    
print("la suma es: ",suma)