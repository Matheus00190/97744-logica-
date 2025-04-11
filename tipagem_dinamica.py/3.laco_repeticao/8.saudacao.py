import os 
os.system("cls || clear")

def calcular_media(n1,n2):
    soma = n1 + n2
    media = soma / 2
    return media 

n1 = float(input("digite a primeira nota:"))
n2 = float(input("digite a segunda nota:"))

media =  calcular_media(n1,n2)

print(f"media: {media}")
        