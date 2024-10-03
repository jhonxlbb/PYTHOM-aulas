import os  
os.system("cls || clear")

from dataclasses import dataclass

@dataclass
class Habitante:
    salario: float
    idade: int
    sexo: str

# Variáveis
print("""
1 | Adicionar pessoa
2 | Exibir resultados
3 | Sair
""")

contador_mulher5000 = 0
lista_habitantes = []

while True:
    menu = input("Escolha uma opção: ")
    match menu:
        case "1":
            idade = int(input("Digite sua idade: "))
            sexo = input("Digite (M) para masculino ou (F) para feminino: ").strip().upper()
            salario = float(input("Digite o seu salário: "))
            
            # Criar uma nova instância de Habitante
            habitante = Habitante(salario=salario, idade=idade, sexo=sexo)
            lista_habitantes.append(habitante)

            # Atualizar contador de mulheres com salário acima de 5000
            if salario > 5000 and sexo == "F":
                contador_mulher5000 += 1

            # Gravar informações no arquivo
            with open("pesquisa_habitantes.txt", "a") as file:
                file.write(f"Idade: {habitante.idade}, Sexo: {habitante.sexo}, Salário: {habitante.salario}\n")

        case "2":
            print("EXIBINDO RESULTADOS!")
            total_habitantes = len(lista_habitantes)

            if total_habitantes > 0:
                total_salario = sum(habitante.salario for habitante in lista_habitantes)
                media_salarial = total_salario / total_habitantes
                maior_idade = max(habitante.idade for habitante in lista_habitantes)
                menor_idade = min(habitante.idade for habitante in lista_habitantes)

                print(f"Média de salário do grupo é de: {media_salarial:.2f}")
                print(f"Maior idade do grupo: {maior_idade}")
                print(f"Menor idade do grupo: {menor_idade}")
                print(f"Quantidade de mulheres com salário acima de 5000: {contador_mulher5000}")

            else:
                print("Nenhum habitante registrado.")

        case "3":
            print("Adeus, mundo.")
            break
