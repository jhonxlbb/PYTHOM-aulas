#limpar o terminal 
import os
os.system("cls || clear")

#solicitando dados 
numero = int(input("Digite um número para saber o mês respectivo do mesmo: "))

#declarando numeros
match(numero):
    case 1:
        print("1-Janeiro")
    case 2:
        print("2-Fevereiro")
    case 3:
        print("3-Março")
    case 4:
        print("4-Abril")
    case 5:
        print("5-Maio")
    case 6:
        print("6-Junho")
    case 7:
        print("7-Julho")
    case 8:
        print("8-Agosto")
    case 9:
        print("9-Setembro")
    case 10:
        print("10-Outubro")
    case 11:
        print("11-Novembro")
    case 12:
        print("12-Dezembro")
    case _:
        print("Somente com números de 1 a 12")