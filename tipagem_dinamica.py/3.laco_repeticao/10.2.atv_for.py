import os 

os.system("cls || clear")
soma = 0
contador = 0

while True:
        nota = float(input(f"digite a nota: "))
        soma += 1
        contador += 1

        resposta = input("dejesa digita mais uma nota? \nresposta com 'S' ou 'N': "). lower()
        if resposta == "n":
                break
        
        media = soma / contador 

        print(f"\media: {media}")




        