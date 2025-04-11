import os 
os.system("cls || clear")

lista_notas = []

for i in range(4):
    nota = float(input("digite uma nota:"))
    lista_notas.append(nota)

media = sum(lista_notas) / 3

print()
for nota in lista_notas: 
    print(f"nota:{nota}")

print()
print(f"media: {media}")


if media < 7:
    resultado = "reprovado!"
else:
    resultado = "aprovado!"    

    print(f"\nMedia: {media}")
    print(f"Resultado: {resultado}")    


