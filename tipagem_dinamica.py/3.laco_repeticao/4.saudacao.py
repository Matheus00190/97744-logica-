import os 
os.system("cls || clear")

def tabuada(numero):
    for i in range(1,11): 
        print(f"{numero} x {i} = {numero * i}")

numero_informado = int(input("digite um numero para tabuada:"))  