import os
import time
os.system("cls || clear")

soma = 0

for i in range(3):
    numero = float(input(f"Digite a {i+1}° nota: "))
    soma = soma + numero 

media = soma / 3
print(f"média: {media}")

if media >= 7:
    print("O aluno está aprovado!")
if media < 7 and media >= 4:
    print("O aluno está em recuperação!")
if media < 4:
    print("O aluno está reprovado!")