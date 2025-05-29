import os 
from dataclasses import dataclass 

os.system('cls || clear')

@dataclass
class Cliente: 
    nome: str 
    bibliografia: str
   

@dataclass
class Autor:
    nome: str 
    titulo: str
    ano: int 


lista_clientes = [] 
QUANTIDADE_AUTORES = 1

print('informe os dados do cliente: ')
for i in range(QUANTIDADE_AUTORES):
    cliente = Autor(
        nome=input('nome:'),
        biblioteca=input('biblioteca:'),
       titulo=input('titulo:'),
       ano=input('ano:')
    )
    lista_clientes.append(cliente)
    print()

print('\n= exibindo dados cliente =')
for cliente in lista_clientes:
    print(f'nome: {cliente.nome}')
    print(f'biblioteca: {cliente.biblioteca}')
    print(f'titulo: {cliente.titulo}')
    print(f'ano: {cliente.ano}')
    print()