
"""
﻿

Escreva um algoritmo que pergunte ao usuário se deseja inserir mais uma nota, se a resposta do usuário for "N",
o programa fará a média aritmética das notas informadas e mostrará a média aritmética para o usuário.
Obs.: Use um contador dentro do laço de repetição para contar a quantidade de iterações (loops).

"""
import os
os.system("cls || clear")

contador = 0
soma = 0

while True:
    nota = float(input("Digite uma nota: "))
    contador += 1
    soma += nota

    resposta = input("Deseja inserir mais uma nota?: ").upper()

    if resposta == "N":
        break
media = soma / contador
print(f"Média: {media}")

