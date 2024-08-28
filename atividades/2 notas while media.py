"""
Escreva um algoritimo que solicite duas notas para um aluno.
Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
calcule e mostre a média aritimética do aluno.
"""

import os
os.system("cls || clear")

soma = 0

for i in range(2):
    while True:
        nota = float(input(f"Digite a {i+1}° nota: "))
    
    if nota > 0 and nota < 10:
        break
   

print(f"média: {media}")
