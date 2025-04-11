import os 

os.system("cls || clear")
soma = 0
contador = 0

while True:
        nota = int(input(f"digite o numero: "))

        if nota > 0:
                soma += nota 
                contador += 1 
        else:
            break                

media = soma / contador 

print(f"\nmedia: {media}")
        
