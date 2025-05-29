import os
import csv
os.system("cls || clear")

class Funcionario:
    def __init__(self, nome, cpf, cargo, salario):
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Cargo: {self.cargo}, Salário: R$ {self.salario:.2f}"

def exibir_menu():
    print("\n--- Menu DENDÊ TECH ---")
    print("1. Cadastrar Funcionário")
    print("2. Listar Funcionários")
    print("3. Atualizar Funcionário")
    print("4. Excluir Funcionário")
    print("5. Salvar Dados")
    print("6. Carregar Dados")
    print("7. Sair")
    print("-----------------------")

def cadastrar_funcionario(lista_funcionarios):
    print("\n--- Cadastrar Funcionário ---")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    cargo = input("Cargo: ")
    while True:
        try:
            salario = float(input("Salário: "))
            break
        except ValueError:
            print("Salário inválido. Digite um valor numérico.")

    funcionario = Funcionario(nome, cpf, cargo, salario)
    lista_funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")

def listar_funcionarios(lista_funcionarios):
    if not lista_funcionarios:
        print("\nNão há funcionários cadastrados.")
        return

    print("\n--- Lista de Funcionários ---")
    for funcionario in lista_funcionarios:
        print(funcionario)

def atualizar_funcionario(lista_funcionarios):
    if not lista_funcionarios:
        print("\nNão há funcionários cadastrados para atualizar.")
        return

    print("\n--- Atualizar Funcionário ---")
    cpf_busca = input("Digite o CPF do funcionário que deseja atualizar: ")
    for i, funcionario in enumerate(lista_funcionarios):
        if funcionario.cpf == cpf_busca:
            print(f"\nDados atuais de {funcionario.nome}:")
            print(funcionario)
            print("\n--- Novas informações (deixe em branco para manter o valor atual) ---")
            novo_nome = input(f"Novo nome ({funcionario.nome}): ")
            novo_cargo = input(f"Novo cargo ({funcionario.cargo}): ")
            while True:
                novo_salario_str = input(f"Novo salário (R$ {funcionario.salario:.2f}): ")
                if not novo_salario_str:
                    novo_salario = None
                    break
                try:
                    novo_salario = float(novo_salario_str)
                    break
                except ValueError:
                    print("Salário inválido. Digite um valor numérico ou deixe em branco.")

            if novo_nome:
                funcionario.nome = novo_nome
            if novo_cargo:
                funcionario.cargo = novo_cargo
            if novo_salario is not None:
                funcionario.salario = novo_salario

            print("Funcionário atualizado com sucesso!")
            return

    print(f"Funcionário com CPF '{cpf_busca}' não encontrado.")

def excluir_funcionario(lista_funcionarios):
    if not lista_funcionarios:
        print("\nNão há funcionários cadastrados para excluir.")
        return

    print("\n--- Excluir Funcionário ---")
    cpf_excluir = input("Digite o CPF do funcionário que deseja excluir: ")
    for i, funcionario in enumerate(lista_funcionarios):
        if funcionario.cpf == cpf_excluir:
            del lista_funcionarios[i]
            print(f"Funcionário com CPF '{cpf_excluir}' excluído com sucesso!")
            return

    print(f"Funcionário com CPF '{cpf_excluir}' não encontrado.")

def salvar_dados(lista_funcionarios, nome_arquivo="funcionarios.csv"):
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(['Nome', 'CPF', 'Cargo', 'Salário']) # Cabeçalho
            for funcionario in lista_funcionarios:
                writer.writerow([funcionario.nome, funcionario.cpf, funcionario.cargo, funcionario.salario])
        print(f"Dados salvos com sucesso em '{nome_arquivo}'.")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def carregar_dados(nome_arquivo="funcionarios.csv"):
    lista_funcionarios = []
    if os.path.exists(nome_arquivo):
        try:
            with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
                reader = csv.reader(arquivo_csv)
                next(reader) # Pular o cabeçalho
                for row in reader:
                    if len(row) == 4:
                        nome, cpf, cargo, salario_str = row
                        try:
                            salario = float(salario_str)
                            funcionario = Funcionario(nome, cpf, cargo, salario)
                            lista_funcionarios.append(funcionario)
                        except ValueError:
                            print(f"Erro ao carregar funcionário com dados: {row}. Salário inválido.")
                    else:
                        print(f"Erro ao carregar linha com número incorreto de campos: {row}")
            print(f"Dados carregados com sucesso de '{nome_arquivo}'.")
        except FileNotFoundError:
            print(f"Arquivo '{nome_arquivo}' não encontrado. Iniciando com uma lista vazia.")
        except Exception as e:
            print(f"Erro ao carregar os dados: {e}")
    else:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Iniciando com uma lista vazia.")
    return lista_funcionarios

def main():
    lista_funcionarios = carregar_dados()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_funcionario(lista_funcionarios)
        elif opcao == '2':
            listar_funcionarios(lista_funcionarios)
        elif opcao == '3':
            atualizar_funcionario(lista_funcionarios)
        elif opcao == '4':
            excluir_funcionario(lista_funcionarios)
        elif opcao == '5':
            salvar_dados(lista_funcionarios)
        elif opcao == '6':
            lista_funcionarios = carregar_dados()
        elif opcao == '7':
            print("Saindo do sistema DENDÊ TECH. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

