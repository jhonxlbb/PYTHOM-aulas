import os
os.system("cls || clear")

#declarando variaveis

#coletando informaçoes
numero1 = float(input("Primeiro número: "))
numero2 = float(input("Segundo número: "))

#calculando 
soma = numero1 + numero2
media = soma / 2
produto = numero1 * numero2

maior: float
menor: float
if (numero1 > numero2):
    maior = numero1
    menor = numero2
else:
    maior = numero2
    menor = numero1

#exibindo resultados
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"A média dos números é igual a: {media}")
print(f"A soma dos números é igual a: {soma}")
print(f"O produto é igual a {produto}")
