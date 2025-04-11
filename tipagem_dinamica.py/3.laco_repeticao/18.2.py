import os 
os.system("cls || clear")

lista_notas = []

for i in range(3):
    nota = float(input("digite uma nota:"))
    lista_notas.append(nota)

media = sum(lista_notas) / 3 

print()
for nota in lista_notas: 
    print(f"nota:{nota}")

print()
print(f"media: {media}")

print()
print(f"somente a segunda nota: {lista_notas[1]}")

