import os 

os.system("cls || clear")

soma = 0

for i in range(3):
    while True:
        nota = float(input(f"digite a {i+1}ª nota:"))

        if nota < 0 or nota > 10:
            nota > 7
            nota < 5
            
            print("nota invalida, tente novamente.\n")
        else:
            soma += nota
            break
        
media  = soma / 2 
print(f"media: {media}")          