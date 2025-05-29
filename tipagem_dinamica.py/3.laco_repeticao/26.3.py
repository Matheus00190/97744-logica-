import os 
from dataclasses import dataclass 

os.system('cls || clear')

@dataclass
class Endereco: 
    logradouro: str 
    numero: int 

    @dataclass
    class pessoa: 

        nome:str
    idade: int 
endereco: Endereco

def exibir_dados(self):
        print(f'nome:{self.nome}')
        print(f'idade:{self. idade}')
        print(f'Endereco: {self.endereco.logradouro}, numero: {self.endereco.numero}')

endereco1 = Endereco('rua A', 23)   
pessoa1 = pessoa('marta', 44, endereco1)
pessoa1.exibir_dados()

print()

endereco2 = Endereco('rua B', 47)
pessoa2 = pessoa('mario', 50, endereco2)
pessoa2.exibir_dados()



 