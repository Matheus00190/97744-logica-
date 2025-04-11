import os 
os.system("cls || clear")

def verificar(numero):
    if numero % 2 == 0:
        print("o numero e par.")
    else:
        print("o numero e impar.")      


print("verificando se um numero e par ou impar.")
numero = int(input("digite um numero:"))
verificar(numero)