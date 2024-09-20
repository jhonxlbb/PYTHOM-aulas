import os 
os.system("cls || clear")

QUANTIDADE_NUMEROS = 5
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        quantidade_pares += 1
    else:
        quantidade_impares +=1
    if numero < 0:
        quantidade_negativos += 1
    else:
        quantidade_positivos += 1

print(f"Quantidade de números positivos: {quantidade_positivos}")
print(f"Quantidade de Números negativos: {quantidade_negativos}")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de impares: {quantidade_impares}")

