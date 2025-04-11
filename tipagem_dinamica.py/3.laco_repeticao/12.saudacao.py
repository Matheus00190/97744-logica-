import os
from datetime import datetime 
os.system("cls || clear")

def calcular_idade(ano_nascimento):
    return datetime.now().year - ano_nascimento

ano_nascimento = int(input("digite o seu ano de nascimento:"))

idade = calcular_idade(ano_nascimento)

print(f"idade: {idade}")