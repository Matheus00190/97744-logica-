import os 
 
os. system("cls || clear")


par = 0
impar = 0


for i in range(5):
    numero = int(input("digite o numero:"))
    if numero % 2 == 0: 
        pares += 1
    else:
        impares += 1        

    print()
    print(f"quantidades de pares: {pares}")
    print(f"quantidades de impares: {impares}")
    

                 

