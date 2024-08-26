#comando para limpar o terminal
import os
os.system("cls || clear")

#coletando informaçoes

login = input("digite seu nome: ")
senha = input("Digite sua senha: ")

#calculando e exibindo resultados

if login == "jhones" and senha == "joao123":
    print("Bem-Vindo!")
else:
    print("Login ou senha inválidos.")