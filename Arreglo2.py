from cgitb import reset
from pickletools import TAKEN_FROM_ARGUMENT1


listaEst = []
resp = "SI"
while(resp.upper() != "NO"):
    tamanio = len(listaEst)
    print("Elementos guardados: ", tamanio)
    nombres = input("Escriba el nombre del estudiante: ")
    listaEst.append(nombres)
    resp = input("Desea agregar mas? SI - NO: ")

for est in listaEst:
    print(est)