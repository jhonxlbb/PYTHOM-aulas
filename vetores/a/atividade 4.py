import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 5
lista_numeros = []

for i in range(QUANTIDADE_NOTAS):
    numero = float(input(f"Digite o {1+i}º número: "))
    lista_numeros.append(numero)

maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)

for contador, nota in enumerate(lista_numeros):
    print(f"{contador+1}ª nota: {nota}")
print(f"Maior número: {maior_numero}")
print(f"\nMenor número: {menor_numero}")