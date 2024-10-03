# Leonardo Araujo, João Filipe

import os 
os.system("cls || clear")

from dataclasses import dataclass

@dataclass
class Habitantes:
    salario: float
    idade: int
    sexo: str


#variaveis




print("""
1 | Adicionar pessoa
2 | Exibir resultados
3 | Sair
      """)

feminino = 0
masculino = 0
contador_mulheres = 0
contador_habitantes = 0
contador_mulher5000 = 0

#calculos
lista_salarial = []
lista_idade = []
lista_habitantes = []
lista_mulheres_5000 = []
while True:

    menu = input("Escolha uma opção: ")
    match menu:
        case "1":
            habitante = Habitantes(            
            idade = int(input("Digite sua idade: ")),
            sexo = input("Digite (M) para masculino ou (F) para feminino: "),
            salario = float(input("Digite o seu salário: "))
            )
            lista_salarial.append(habitante.salario)
            lista_habitantes.append(habitante)
            lista_idade.append(habitante.idade)
            with open("pesquisa_habitantes.txt", "r") as file:
                for habitante in lista_habitantes:
                    if habitante.salario > 5000 and habitante.sexo == "F":
                        contador_mulher5000 += 1

            with open("pesquisa_habitantes.txt", "a") as file:
                for habitante in lista_habitantes:
                    file.write(f"{contador_mulher5000},{habitante.idade},{habitante.sexo},{habitante.salario}\n")

        case "2":
            print("EXIBINDO RESULTADOS!")
            

            total_habitantes = len(lista_salarial)
            total_salario = sum(lista_salarial)
            media_salarial = total_salario / total_habitantes
            maior_idade = max(lista_idade)
            menor_idade = min(lista_idade)

            print(f"Média de salário do grupo é de: {media_salarial}")
            print(f"Maior idade do grupo: {maior_idade}")
            print(f"Menor idade do grupo: {menor_idade}")
            print(f"Quantidade de mulheres com salário a partir de 5Mil R$: {contador_mulher5000} ")

        case "3":
            print("adeus mundo")
            break
 #calculos       


