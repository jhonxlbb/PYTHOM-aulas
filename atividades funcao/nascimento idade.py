import os 
os.system("cls || clear")

ano = int(input("Digite o ano em que nasceu: "))

def idade(n1):
    idade = 2024 - n1
    return idade

atual = idade(ano)

print(f"a iade é: {atual}")