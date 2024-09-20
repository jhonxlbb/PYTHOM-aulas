import os 
os.system("cls || clear")

lista_numeros = []
contador = 0
for i in range(6):
    numero = int(input("digite um número:"))
    if numero > 0 and numero % 2 == 0:
        contador += 1
    else:
        print("O Número digitado não atende aos requisitos ")
        break
    lista_numeros.append(numero)

for numero in reversed(lista_numeros):
    print(numero) 