import os 
from dataclasses import dataclass 

os.system('cls || clear')

@dataclass
class funcionario: 
 
    nome: str 
    data_admissao: str 
    matricula: str 
    endereco: str 


@dataclass
class Cliente:
    nome: str
    data_nascimento:str
    endereco:str

    lista_de_cliente = []
    
    lista_de_funcionario = []
    

    for i in range(1):
        print("digite os dados do funcionario:")
    Cliente = funcionario(
    nome = input("nome:"),
    data_administracao = input("data de administracao:"),
    matricula = input("matricula:"),
    endereco = int(input("endereco:"))
)
    lista_de_cliente.append(funcionario)
print()

nome_arquivo = "dados_cliente.csv"

print( "Salvando dados no arquivo")
with open(nome_arquivo,"a") as arquivo_funcionario:
    for cliente in funcionario:
        arquivo_funcionario.write(f"{cliente.nome}, {cliente.endereco}, {cliente.data_nascimento},\n")

        print("salvo com sucesso.")

print("\nAcessando dados do arquivo. ")
try:
    with open(nome_arquivo, "r") as arquivo_cliente:
     linhas = arquivo_cliente.readlines()
    for linha in linhas:
            print(f" - {linha.strip()}")
except FileNotFoundError:
    print("o arquivo nao foi encontrado.")
