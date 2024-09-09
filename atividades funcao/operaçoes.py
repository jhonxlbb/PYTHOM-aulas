import os 
os.system("cls || clear")

def operacoes(n1, n2):
    soma = n1 + n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2
    divisao = n1 / n2
    return soma, subtracao, multiplicacao, divisao

numero1 = int(input("digite um numero: "))
numero2 = int(input("digite um numero: "))
operacao = input("operaçao: ")
