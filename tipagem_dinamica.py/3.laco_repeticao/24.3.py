import os 
from dataclasses import dataclass 

os.system('cls || clear')

@dataclass
class pessoa: 
    nome: str
    idade: int

pessoa1 = pessoa('alice', 17)
pessoa2 = pessoa('bob', 19)

@dataclass
class pet:
    nome: str
    idade: int
    peso: float
    


pet1 = pet('toto',4, 7.8)
pet2 = pet('tubarao',6, 9.2)

print('\n= dados da pessoa =')
print(f'nome: {pessoa1.nome} . idade: {pessoa1.idade} anos. ')
print(f'nome: {pessoa2.nome} . idade: {pessoa2.idade} anos.')

print('\n= dados da pessoa =')
print(f'nome: {pet1.nome} . idade: {pet1.idade} anos.')
print(f'nome: {pet2.nome} . idade: {pet2.idade} anos.')
