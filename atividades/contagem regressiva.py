import os
import time

os.system("cls || clear")

numero = int(input("Digite um numero: "))

for i in range(numero, 0, -1):
    print(i)
    time.sleep(1) #vai esperar um segundos

print("===FIM===")