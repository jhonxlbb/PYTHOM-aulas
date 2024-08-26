import os
import time
os.system("cls || clear")

soma = 0

for i in range(5):
    numero = int(input(f"Digite o {i+1}° número: "))
    soma = soma + numero 

print(f"resultado: {soma}")