"""
5) Escreva um programa que inverta os caracteres de um string.
"""

string = "python"
metodo1 = string[::-1]
print(f"Metodo 1: {metodo1}")

index = len(string) - 1
metodo2 = ""
while index >= 0:
  metodo2 += string[index]
  index -= 1
print(f"Metodo 2: {metodo2}")

