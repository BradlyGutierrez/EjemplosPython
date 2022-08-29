#Sumar los elementos de un arreglo
arreglo = []
cantidad = int(input("Dime cuantos numeros: "))
cont = 0
while(cont< cantidad):
    num = int(input("Dime un numero: "))
    arreglo.append(num)
    cont +=1
    
suma = 0
for num in arreglo: 
    suma += num

print("La suma es ", suma)
