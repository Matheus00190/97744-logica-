import os
os.system("cls || clear")

lista_de_numero = []
QUANTIDADE = 5 

print("= LISTA DE COMPRAS =")
for i in range(QUANTIDADE):
    numero = int(input("digite um numero para lista:"))
    lista_de_numero.append(numero)

menor = min(lista_de_numero)
maior = max(lista_de_numero)

print("\n= ITENS DA LISTA =")
for i, numero in enumerate(lista_de_numero, start=1):
    print(f"{i}: {numero}")

print(f"maior numero: {maior}")
print(f"menor numero: {menor}")