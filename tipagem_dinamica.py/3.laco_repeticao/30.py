import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass
class Carro:
    marca:str
    modelo:str
    categoria:str
    preco:float

listas_carros = []
QUANTIDADE_CLIENTES = 2

print('informe os dados do carros1: ')
for i in range(QUANTIDADE_CLIENTES):
    carros = Carro(
        carro=input('carro:'),
        modelo=input('modelo:'),
        categoria=input('categoria:'),
        preco=input('preco:')
    )
    listas_carros.append(carros1)
    print()

    print("\n= exibindo dados dos carros =")
    for carros1 in listas_carros:
     print(f"carro: {carros1.carro}")
     print(f"modelo: {carros1.modelo}")
     print(f'categoria: {carros1.categoria}')
     print(f'preco: {carros1.preco}')
     print()

    print ("= Salvando os dados dos carros =")
    nome_arquivo = "dados_clientes.txt"
def salvar_carros(lista):
    nome_arquivo = "dados_carros.txt"

    with open(nome_arquivo, "a") as arquivo_clientes:
        for cliente in lista:
            arquivo.write(f"{carros1.carro},{carros1.modelo},{carros1.categoria},{carros1.preco}\n")

    print("Dados dos clientes salvos com sucesso.")


    
