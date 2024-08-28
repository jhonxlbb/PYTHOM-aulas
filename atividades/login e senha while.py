"""
crie um programa que solicite do usuario seu login e um senha.

O programa deve continuar pedindo o login e senha até que ambos estejam corretos.

"""

import os
os.system("cls || clear")

contador = 0

while True:
    login = input("login: ").lower().strip()
    senha = input("senha: ").lower().strip()
    contador = contador + 1

    if login == "joao" and senha == "123":
        print("BEM VINDO")
        break
    else:
        print("acesso negado")
        print(f"Tentativa: {contador}")
        if contador == 3:
            print("numero maximo de tentativas atingido")
            break
           
