import os
os.system("cls || clear")

def calcular_media(lista):
    media = sum(lista) / len(lista)
    return media

lista_notas = []
QUANTIDADE_NOTAS = 2

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f'digite a {i+1}ª nota'))
    lista_notas.append(nota)

media = calcular_media(lista_notas)

print(f"\nmedia: {media}")
