import os 
from dataclasses import dataclass 

os.system('cls || clear')

@dataclass
class cliente: 
    nome: str 
    emeil: str
    telefone:str

lista_clientes = [] 
QUANTIDADE_CLIENTES = 2

print('informe os dados do cliente: ')
for i in range(QUANTIDADE_CLIENTES):
    cliente = cliente(
        nome=input('nome:'),
        emeil=input('E-mail:'),
        telefone=input('telefone:')
    )
    lista_clientes.append(cliente)
    print()

print('\n= exibindo dados cliente =')
for cliente in lista_clientes:
    print(f'nome: {cliente.nome}')
    print(f'E-mail: {cliente.email}')
    print(f'telefone: {cliente.telefone}')
    print()

