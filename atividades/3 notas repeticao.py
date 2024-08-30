import os
os.system("cls || clear")

"""
Escreva um algoritmo que leia três notas de um aluno.
Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
Após receber as notas dentro dos parâmetros acima, calcule a média e verifique se o aluno está aprovado, recuperação ou reprovado considerando os seguintes critérios:
Se a média for a partir de 7, aprovado;
Se a média for entre 5 e 6,9, o aluno está em recuperação; Caso seja menor que 5, o aluno está reprovado.
"""
soma = 0 #definindo um valor para que não apareça o erro NaN
media = 0 #definindo um valor para que não apareça o erro NaN

for i in range (3): #replica 3x oque eu fiz abaixo
    nota = float(input(f"Digite a {i+1}º nota: ")) #defini que a nota é oque o usuario digitar
    if nota <= 10 and nota >= 0: #criando uma condição para que o algoritimo prossiga
        soma = soma + nota
        media = soma / 3
    else:
        print("A sua nota não está entre 0 e 10.") 
        break # comando utilizado para finalizar o codigo

print(f"Sua média é: {media}")
if media >= 7:
    print("Aprovado!")
elif media >= 5 and media < 7: #funciona como outro if.
    print("Recuperação!")
else:
    print("Reprovado!")
