import os
os.system("cls || clear")

def situacao(n1):
    if n1 >= 7:
        return "aprovado"
    elif n1 >= 5 and n1 < 7:
        return "recuperação"
    else:
        return "reprovado"
    

QUANTIDADE_NOTAS = 3

lista_notas = []

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite a {i+1}º nota: "))
    lista_notas.append(nota)
    
#processamento
soma = sum(lista_notas)
media = soma / QUANTIDADE_NOTAS
situacao_aluno = situacao(media)

for i, nota in enumerate(lista_notas):
    print(f"a {i+1}º nota é: {nota}")

print(f"A média do aluno é: {media}")
print(f"A situação do aluno: {situacao_aluno}")