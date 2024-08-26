import os
os.system("cls || clear")


print("""
CÓDIGO |     PRATO      |  VALOR  
__________________________________
                                  |
   1   |    picanha     | 25,00 R$|
   2   |    lasanha     | 20,00 R$|
   3   |   strogonoff   | 18,00 R$|
   4   | bife acebolado | 15,00 R$|
   5   |   pão com ovo  | 05,00 R$|
__________________________________|    

      
        
        """)

opcao = input("Digite o código do pedido: ")

match(opcao):
    case "1":
        print(" prato: picanha  | 25,00 R$")
    case "2":
        print(" prato: lasanha | 20,00 R$")
    case "3":
        print(" prato: strogonoff | 18,00 R$")
    case "4":
        print(" prato: bife acebolado | 15,00 R$")
    case "5":
        print(" prato: pão com ovo  | 05,00 R$")