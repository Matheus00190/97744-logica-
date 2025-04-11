import os 
import time 
os. system("cls || clear")

numero = int(input("digite o numero pra contagem regressiva:"))

print(f"\niniciando contagem:")
for i in range(numero,0,-1):
    print(f"{i}")
    time.sleep(4)
