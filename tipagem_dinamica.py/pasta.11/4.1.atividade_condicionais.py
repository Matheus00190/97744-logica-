import os 

os.system("clear")

#utilizando condicionais anilhas.
primeira_nota = float(input("digite a primeira nota: "))
primeira_nota = float(input("digite a segunda nota: "))
primeira_nota = float(input("digite a terceira nota: "))

media = (primeira_nota + segunda_nota + terceira_nota) /3

print()

print(f"Media: {media}")   

if media < 7:
    resultado = "reprovado!"
else:
    resultado = "aprovado!"    

    print(f"\nMedia: {media}")
    print(f"Resultado: {resultado}")    
