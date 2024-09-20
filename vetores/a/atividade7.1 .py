import os 
os.system("cls || clear")

lista_numeros = []

contador = 0

while True:
    numero = int(input("Digite um numero: "))
    if numero > 0 and numero % 2 == 0:
        contador = contador + 1
    else:
        
        print("o número digitado não atende aos requisitos")
    lista_numeros.append(numero)
    if contador == 6:
        break

for numero in reversed(lista_numeros):
    print(numero)
