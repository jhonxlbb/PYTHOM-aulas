import os
os.system("cls || clear")

#declarando variaveis
soma: float 
media: float
#solicitando dados
nome = input("digite seu nome: ")
idade = int(input("Digite sua idade: "))
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))

#calculando
soma = (nota1 + nota2 + nota3)
media = soma / 3
#exibindo resultados 
if media >= 7 :
    print("O aluno está APROVADO!!!")
else:
    print("O aluno está REPROVADO!!!")