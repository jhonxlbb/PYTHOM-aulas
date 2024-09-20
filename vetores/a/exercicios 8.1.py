import os 
os.system("cls || clear")

QUANTIDADE_NUMEROS = 5
quantidade_pares_positivos = 0
quantidade_impares = 0
quantidade_negativos = 0
quantidade_inseridos = 0


while True:
    numero = int(input("Digite um número inteiro: "))
    quantidade_inseridos += 1
    if numero % 2 == 0 and numero > 0:
        quantidade_pares_positivos += 1
    else:
        quantidade_impares +=1
    if numero < 0:
        quantidade_negativos += 1
    if numero == 0:
        break


