import os 
os.system("cls || clear")

lista_de_numeros = []
QUANTIDADE = 6

def maior_menor(lista):
    menor = min(lista)
    maior = max(lista)
    return menor, maior

def solicitacao_dados():
    print("= LISTA DE COMPRA =")
    for i in range(QUANTIDADE):
        numero = int(input("digite um numero para lista:"))
        lista_de_numeros.append(numero)

def mostrar_dados():
    print("\n=INTENS DA LISTA =")
    for i, numero in enumerate(lista_de_numeros, start=1):
        print(f"{i}: {numero}")

    print(f"maior numero: {maior}")
    print(f"menor numero: {menor}")

    solicitacao_dados()
    menor, maior = maior_menor(lista_de_numeros)
    mostrar_dados()