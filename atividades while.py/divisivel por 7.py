import os 
os.system("cls || clear")

# Começa com o número 51, pois precisamos encontrar um número maior que 50
numero = 51

# Laço while para encontrar o número divisível por 7
while numero % 7 != 0:
    numero += 1  # Add o número até encontrar um que seja divisível por 7

print(f"O primeiro número maior que 50 que é divisível por 7 é: {numero}")
