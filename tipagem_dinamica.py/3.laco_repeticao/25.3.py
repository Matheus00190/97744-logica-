import os 
from dataclasses import dataclass 

os.system('cls || clear')

@dataclass
class pessoa: 
    nome: str
    idade: int
    peso: float
    altura: float

pessoa1 = pessoa(
    nome = input('digite o nome:'),
    idade = int(input('digite a idade:')),
    peso = float(input('digite o peso:')),
    altura = float(input('digite a altura:'))
    )
   
print()

pessoa2 = pessoa(
    nome = input('digite o nome:'),
    idade = int(input('digite a idade:')),
    peso = float(input('digite o peso:')),
    altura = float(input('digite a altura:'))
    )


print(f'nome: {pessoa1.nome} , idade: {pessoa1.idade} anos. ')
print(f'nome: {pessoa2.nome} , idade: {pessoa2.idade} anos.') 

