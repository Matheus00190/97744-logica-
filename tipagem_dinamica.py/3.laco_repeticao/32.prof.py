import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Funcionario:
    nome: str
    data_admissao: str
    matricula: str
    endereco: str
     
   
@dataclass
class Cliente:
    nome: str
    data_nascimento: str
    endereco: str
   
def salvar_funcionarios(lista):
    nome_arquivo = "dados_funcionarios.csv"

    with open(nome_arquivo, "a") as arquivo_fucionarios:
        for funcionario in lista:
            arquivo_fucionarios.write(f"{funcionario.nome}, {funcionario.data_admissao}, {funcionario.matricula}, {funcionario.endereco}\n")
   
    print("Dados dos funcionários salvos com sucesso.")
       
def salvar_clientes(lista):
    nome_arquivo = "dados_clientes.csv"

    with open(nome_arquivo, "a") as arquivo_clientes:
        for cliente in lista:
            arquivo_clientes.write(f"{cliente.nome}, {cliente.data_nascimento}, {cliente.endereco}\n")
   
    print("Dados dos clientes salvos com sucesso.")
       
   
lista_funcionarios = []
lista_clientes = []
   
for i in range(1):
    print("Digite os dados do funcionário: ")
    funcionario = Funcionario(
        nome= input("Nome: "),
        data_admissao=input("Data de nascimento: "),
        matricula=input("Matrícula: "),
        endereco=input("Endereço: ")
    )
    lista_funcionarios.append(funcionario)
    print()
   
    print("Digite os dados do cliente: ")
    cliente = Cliente(
        nome=input("Nome: "),
        data_nascimento=input("Data de nascimento: "),
        endereco=input("Endereço: ")
    )
    lista_clientes.append(cliente)
    print()
   
       
salvar_funcionarios(lista_funcionarios)
salvar_clientes(lista_clientes)
