import os 
import time


os.system("cls || clear")

contador = 0
soma_salario = 0
maior_idade = 0
menor_idade = 9999
mulheres5k = 0


while True:
    print("""
codigo | descricao 
1      | adicionar pessoas
2      | exibir resultados
3      | sair   
""")
    opcao = int(input("dite a opcao desejada: "))

    match opcao: 
        case 1: 
            idade = int(input("informe a idade:"))
            sexo = input(("informe o sexo com 'M' ou 'f': "))
            salario = float(input("informe o salario:"))
            contador += 1 
            soma_salario += salario 

            if idade > maior_idade:
                maior_idade = idade

            if idade < menor_idade:
                menor_idade = idade 

            if sexo == "F" and salario >= 5000:
                mulheres5k += 1 
            os.system("cls || clear")
            
        
        case 2 :
            if contador > 0: 
                media_salario_grupo = soma_salario / contador
                print("\n= exibindo resultados = ")
                print(f" media de salario do grupo: {media_salario_grupo}")
                print(f"maior idade do grupo: {maior_idade}")
                print(f"menor idade do grupo: {menor_idade}")
                print(f"quantidade mulheres com salario aparti de 5 mil: {mulheres5k}")

            else:
                print("nao existem dados para exibir.")

            time.sleep(3)
            os.system("cls || clear")
            

        case 3:
            print("\nfim do programa.")
            break
        case _: 
            print("\nopcao invalida.")
            time.sleep(3)
            os.system("cls || clear")




           