import os
import time
os.system("cls || clear")

soma = 0

for i in range(4):
    numero = float(input(f"Digite a {i+1}° nota: "))
    soma = soma + numero 

media = soma / 4
print(f"média: {media}")

