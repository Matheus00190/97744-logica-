import os 
os.system("cls || clear")

lista_numero = []

for i in range(5):
    numero = float(input("digite um numero:"))
    lista_numero.append(numero)


print()
for numero in lista_numero:
    print(f"numero:{numero}")

print()
print(f"somente o maior numero: {lista_numero[1]}")