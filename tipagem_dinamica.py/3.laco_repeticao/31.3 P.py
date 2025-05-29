import os 
from dataclasses import dataclass 

os.system("cls || clear")

@dataclass
class paciente: 
    nome: str 
    idade: int
   
lista_de_paciente = []

for i in range(2):
 print("digite os dados do paciente:")
paciente = paciente(
    nome = input("nome:"),
    idade = int(input("idade:"))
)
lista_de_paciente.append(paciente)
print()

nome_arquivo = "dados_pacientes.csv"


print( "Salvando dados no arquivo")
with open(nome_arquivo,"a") as arquivo_paciente:
    for paciente in lista_de_paciente:
        arquivo_paciente.write(f"{paciente.nome}, {paciente.idade}\n")

print("salvo com sucesso.")

print("\nAcessando dados do arquivo. ")
try:
    with open(nome_arquivo, "r") as arquivo_paciente:
     linhas = arquivo_pacientes.readlines()
    for linha in linhas:
            print(f" - {linha.strip()}")
except FileNotFoundError:
    print("o arquivo nao foi encontrado.")