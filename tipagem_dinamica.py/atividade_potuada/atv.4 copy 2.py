import os
import csv

# Limpa a tela do terminal
os.system("cls || clear")

# Classe para representar um funcionário
class Funcionario:
    def __init__(self, nome, cpf, cargo, salario, funcao):
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.salario = salario
        self.funcao = funcao

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: {self.salario}")
        print(f"Função: {self.funcao}")
        print()

# Função para verificar se a lista está vazia
def verificar_lista_vazia(lista):
    if not lista:
        print("\nA lista está vazia.")
        return True
    return False

# Função para adicionar um novo funcionário
def adicionar(lista):
    print("= Digite os dados do funcionário = ")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    cargo = input("Cargo: ")
    salario = input("Salário: ")
    funcao = input("Função: ")
    funcionario = Funcionario(nome, cpf, cargo, salario, funcao)
    lista.append(funcionario)
    print("Funcionário adicionado com sucesso.")

# Função para mostrar todos os funcionários na lista
def mostrar_funcionarios(lista):
    if verificar_lista_vazia(lista):
        return

    print("\n= Lista de funcionários =")
    for funcionario in lista:
        funcionario.mostrar_dados()

# Função para atualizar os dados de um funcionário existente
def atualizar(lista):
    if verificar_lista_vazia(lista):
        return

    nome_atualizar = input("Digite o nome do funcionário que deseja atualizar: ")
    encontrado = False

    for funcionario in lista:
        if funcionario.nome == nome_atualizar:
            print("= Digite os novos dados do funcionário = ")
            funcionario.nome = input("Novo Nome: ")
            funcionario.cpf = input("Novo CPF: ")
            funcionario.cargo = input("Novo Cargo: ")
            funcionario.salario = input("Novo Salário: ")
            funcionario.funcao = input("Nova Função: ")
            encontrado = True
            print("Funcionário atualizado com sucesso.")
            break

    if not encontrado:
        print(f"\nO funcionário com o nome '{nome_atualizar}' não foi encontrado.")

# Função para excluir um funcionário da lista
def excluir(lista):
    if verificar_lista_vazia(lista):
        return

    nome_excluir = input("Digite o nome do funcionário que deseja excluir: ")
    encontrado = False
    for i, funcionario in enumerate(lista):
        if funcionario.nome == nome_excluir:
            del lista[i]
            print("Funcionário excluído com sucesso.")
            encontrado = True
            break
    if not encontrado:
        print("Funcionário não encontrado.")

# Função para salvar os dados dos funcionários em um arquivo CSV
def salvar_csv(lista, nome_arquivo="funcionarios.csv"):
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(['Nome', 'CPF', 'Cargo', 'Salário', 'Função'])  # Escreve o cabeçalho
            for funcionario in lista:
                writer.writerow([funcionario.nome, funcionario.cpf, funcionario.cargo, funcionario.salario, funcionario.funcao])
        print(f"Dados salvos com sucesso em '{nome_arquivo}'.")
    except Exception as e:
        print(f"Erro ao salvar para CSV: {e}")

# Função para carregar os dados dos funcionários de um arquivo CSV
def carregar_csv(nome_arquivo="funcionarios.csv"):
    lista_funcionarios = []
    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            reader = csv.reader(arquivo_csv)
            header = next(reader)  # Lê o cabeçalho
            for row in reader:
                if len(row) == 5:
                    nome, cpf, cargo, salario, funcao = row
                    funcionario = Funcionario(nome, cpf, cargo, salario, funcao)
                    lista_funcionarios.append(funcionario)
                else:
                    print(f"Linha ignorada devido ao formato incorreto: {row}")
        print(f"Dados carregados com sucesso de '{nome_arquivo}'.")
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Iniciando com uma lista vazia.")
    except Exception as e:
        print(f"Erro ao carregar do CSV: {e}")
    return lista_funcionarios

# Função principal que exibe o menu e interage com o usuário
def menu():
    lista_funcionarios = carregar_csv()

    while True:
        print("\n= Menu de Funcionários =")
        print("1. Adicionar Funcionário")
        print("2. Listar Funcionários")
        print("3. Atualizar Funcionário")
        print("4. Excluir Funcionário")
        print("5. Salvar para CSV")
        print("6. Carregar do CSV")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar(lista_funcionarios)
        elif opcao == '2':
            mostrar_funcionarios(lista_funcionarios)
        elif opcao == '3':
            atualizar(lista_funcionarios)
        elif opcao == '4':
            excluir(lista_funcionarios)
        elif opcao == '5':
            salvar_csv(lista_funcionarios)
        elif opcao == '6':
            lista_funcionarios = carregar_csv()
        elif opcao == '7':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Bloco que garante que a função menu() seja chamada apenas quando o script é executado diretamente
if __name__ == "__main__":
    menu()