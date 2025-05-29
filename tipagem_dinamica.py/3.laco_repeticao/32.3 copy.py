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

def salvar_funcionarios(lista):
    nome_arquivo = "dados_funcionario.csv"
    with open(nome_arquivo, "a") as arquivo_funcionario:
        for funcionario in lista:
            arquivo_funcionario.write(f"{funcionario.nome}, {funcionario.data_admissao}, {funcionario.matricula}, {funcionario.endereco}\n")

    print("dados dos funcionarios salvos com sucesso.")

def salvar_clientes(lista):
    nome_arquivo = "dados_clientes.csv"
    with open(nome_arquivo, "a") as arquivo_clientes:
        for clientes in lista:
            arquivo_clientes.write(f"{cliente.nome}, {cliente.data_nascimento}, {cliente.endereco}\n")

    print("dados dos clientes salvos com sucesso.")


lista_de_funcionarios = []
lista_de_clientes = []

for i in range(1):
    print("digite os dados do funcionario:")
    funcionario = Funcionario(
        nome = input("nome: "),
        data_admissao= input("data de admissao:"),
        matricula = input("matricula:"),
        endereco = input("endereco:")
    )
    lista_de_funcionarios.append(funcionario) 
    print()

   
    print("digite os dados do cliente: ")
    cliente = Cliente(
        nome = input("nome:"),
        data_nascimento = input("data de nascimento:"),
        endereco = input("endereco:")
        )
    lista_clientes.append(cliente)
    print()

salvar_funcionarios(lista_funcionarios)
salvar_clientes(lista_clientes)

