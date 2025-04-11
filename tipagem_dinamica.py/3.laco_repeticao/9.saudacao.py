import os 
os.system("cls || clear")

def contar_pares_impares():
    pares = 0 
    impares = 0 

    for i in range(6):
        numero = int(input("digite um numero: "))
        if numero % 2 == 0:
            pares += 1 
        else:
            impares += 1
    return pares, impares 

quantidades_pares, quantidade_impares = contar_pares_impares()

print(f"\nquantidade de pares: {quantidades_pares}")
print(f"\nquantidade de impares: {quantidade_impares}")




















