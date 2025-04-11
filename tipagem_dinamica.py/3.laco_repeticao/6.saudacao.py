import os 
os.system("cls || clear")

def verificacao(numero):
    if numero >= 0:
        print("numero e positivo.")
    else:
        print(" numero e negativo.")      


print("verificando se um numero e positivo ou negativo.")
numero = int(input("digite um numero:"))
verificacao(numero)