import os 

os.system("cls || clear")

login_cadastrado = "marta"
senha_cadastrado = "123"
contador = 0

while True:
    login = input("digite o loguin: ")
    senha = input("digite o senha: ")

    if login_cadastrado == login and senha_cadastrado == senha:
        print("bem-vendo!")
        break 
    else:
        print("acesso negado.\ntente novamente\n")
        contador += 1
        if contador == 3:
            print("numero de tentativas acima do permitido>\n")
            break