import os 


os.system("cls || clear")

while True:
    idade = int(input("diite sua idade: "))

    if idade < 18:
        print("Nao autorizado. \nsomente maiores de 18. \n")
    else:
        break

    print("acesso permitido.")    
    print("fim.")    