import os 
from dataclasses import dataclass 

os.system('cls || clear')

@dataclass
class pessoa: 
    nome: str
    idade: int

pessoa1 = pessoa('alice', 17)
pessoa2 = pessoa('bob', 19)

print(f'nome: {pessoa1.nome} . idade: {pessoa1.idade} anos. ')
print(f'nome: {pessoa2.nome} . idade: {pessoa2.idade} anos.')
