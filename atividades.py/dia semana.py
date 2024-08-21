import os
os.system("cls || clear")

print("""
dias da semana

1 - Domingo
2 - Segunda-Feira
3 - Terça-Feira
4 - Quarta-Feira
5 - Quinta-Feira
6 - Sexta-Feira
7 - Sabádo    

Digite o número de acordo com o dia da semana abaixo!!!       
      """)

dia = int(input("Digite o número: "))

match(dia):
    case 1:
        print("Final de semana.")
    case 2:
        print("Dia útil.")
    case 3:
        print("Dia útil.")
    case 4:
        print("Dia útil.")
    case 5:
        print("Dia útil.")
    case 6:
        print("Dia útil.")
    case 7:
        print("Final de semana.")
    case _:
        print("inválido.")