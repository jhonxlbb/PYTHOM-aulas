import os
os.system("cls || clear")

maior : int
menor : int

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
else:
    segundo_numero = maior
    primeiro_numero = menor

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
