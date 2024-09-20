import os 
os.system("cls || clear")


lista_numeros = []

# solicitando dados
for i in range(5):
    numero = int(input("Digite um número: "))
    if numero < 0:
        numero = 0
    lista_numeros.append(numero)

#exibindo resultados 
for i, nota in enumerate(lista_numeros):
    print(f"{i+1}º número: {nota}")