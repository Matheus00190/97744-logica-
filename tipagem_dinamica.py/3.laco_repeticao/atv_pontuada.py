import os 
os.system("cls || clear")
valor_gorjeta = 0
preco_total = 0
pratos_solicitados = ""

while True:
    print("""
    ================= MENU =================
    1 \t burger \t\tR$ 27,00
    2 \t comida de boteco \t\tR$ 33,00
    3 \t drink \t\tR$ 20,00
    4 \t sobremesa \tR$ 17,00
    5 \t croissant \t\tR$ 15,00
    6 \t ratatouille \t\tR$ 35.00
    7 \t crepes \t\tR$ 25,00
          """)
   
    opcao = int(input("Digite o número da opção desejada: "))
   
    match opcao:
        case 1:
            prato = "burger"
            preco = 27
        case 2:
            prato = "comida de boteco"
            preco = 33
        case 3:
            prato = "drink"
            preco = 20
        case 4:
            prato = "sobremesa"
            preco = 17
        case 5:
            prato = "croissant"
            preco = 15
        case 6:
            prato = "ratatouille"
            preco = 35
        case 7:
            prato = "creps"
            preco = 25
        case _:
            print("Opção inválida. \nTente novamente... \n")
            prato = ""
            preco = 0
   
    preco_total += preco
    pratos_solicitados += ", " + prato if pratos_solicitados else prato
   
    mais_pedidos = input("Deseja fazer um novo pedido?\nUse 'S' or 'N' para responder: ").lower()

    if mais_pedidos == "n":
        break
   
if preco_total > 0:
    gorjeta_garcom = input("Deseja pagar 10% do valor da sua nota como gorjeta para o garçom? ").lower()
    if gorjeta_garcom == "s":
        valor_gorjeta = preco_total * 0.10

total_pagar = preco_total + valor_gorjeta

print("\n=== Nota Fiscal ===")
print(f"Pratos solicitados: {pratos_solicitados}")
print(f"Valor da gorjeta: R$ {valor_gorjeta}")
print(f"Valor total da compra: R$ {total_pagar}")
