import os 
from dataclasses import dataclass 

os.system('cls || clear')

@dataclass
class Cliente: 
    nome: str 
    emeil: str
    telefone:str

lista_clientes = [] 
QUANTIDADE_CLIENTES = 2

print('informe os dados do cliente: ')
for i in range(QUANTIDADE_CLIENTES):
    cliente = Cliente(
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

    # Salvando em um arquivo .txt
print ("= Salvando os dados dos clientes =")
nome_arquivo = "dados_clientes.txt"

# w -> escrita/salvar/sobrescrever
# a -> escrita/salvar/acumular

with open (nome_arquivo, "w") as arquivo:
    for cliente in lista_clientes:
        arquivo.write(f"{cliente.nome},{cliente.email},{cliente.telefone}\n")