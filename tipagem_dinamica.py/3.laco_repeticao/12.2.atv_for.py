import os 
import time 

os.system("cls || clear")
while True:

    print("contagem de 2 + 2.")
    for i in range(2,11,2): 

     print(f"valor variavel i: {i}")
     time.sleep(1)
    
    while True:
        nota = int(input(f"digite o numero: "))

        if nota > 0:
                soma += nota 
                contador += 1 
        else:
            break                

        media = soma / contador 

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
    

                 


   