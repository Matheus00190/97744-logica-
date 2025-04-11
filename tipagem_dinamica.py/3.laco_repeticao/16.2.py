import os 
os.system("cls || clear")

def calcular_media(n1,n2,n3):
    soma = n1 + n2 + n3
    media = soma / 3
    return media 

n1 = float(input("digite a primeira nota:"))
n2 = float(input("digite a segunda nota:"))
n3 = float(input("digite a terceira nota:"))

media =  calcular_media(n1,n2,n3 )

print(f"media: {media}")
        