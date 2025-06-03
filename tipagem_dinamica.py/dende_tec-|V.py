import csv
import os
import time

EMPLOYEES = []  # Lista para armazenar objetos Funcionario
CSV_FILENAME = 'funcionarios.csv'

# --- Definição da Classe ---
class Funcionario:
    """
    Representa um funcionário da empresa DENDÊ TECH.
    """
    def __init__(self, nome, cpf, cargo, salario):
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        """
        Retorna uma representação em string do objeto Funcionario.
        """
        return (f"Nome: {self.nome}\n"
                f"CPF: {self.cpf}\n"
                f"Cargo: {self.cargo}\n"
                f"Salário: R${self.salario:.2f}")

# --- Funções de Persistência de Dados ---
def load_employees_from_csv():
    """
    Carrega os dados dos funcionários de um arquivo CSV para a lista em memória.
    """
    EMPLOYEES.clear()  # Limpa os dados existentes antes de carregar
    if not os.path.exists(CSV_FILENAME):
        print(f"Arquivo '{CSV_FILENAME}' não encontrado. Iniciando com lista vazia.")
        time.sleep(1.5)
        return

    try:
        with open(CSV_FILENAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    # Garante a conversão correta do tipo para salário
                    salario = float(row['salario'])
                    employee = Funcionario(row['nome'], row['cpf'], row['cargo'], salario)
                    EMPLOYEES.append(employee)
                except ValueError:
                    print(f"Aviso: Salário inválido encontrado para o CPF {row.get('cpf', 'N/A')}. Ignorando esta entrada.")
            print(f"Dados de funcionários carregados de '{CSV_FILENAME}' com sucesso.")
            time.sleep(1.5)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{CSV_FILENAME}' não foi encontrado.")
        time.sleep(1.5)
    except Exception as e:
        print(f"Erro ao carregar dados do CSV: {e}")
        time.sleep(1.5)

def save_employees_to_csv():
    """
    Salva os dados dos funcionários da lista em memória para um arquivo CSV.
    """
    if not EMPLOYEES:
        print("Nenhum funcionário para salvar. O arquivo CSV será criado/atualizado vazio.")
        time.sleep(1.5)

    try:
        with open(CSV_FILENAME, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['nome', 'cpf', 'cargo', 'salario']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()  # Escreve a linha de cabeçalho
            for employee in EMPLOYEES:
                writer.writerow({
                    'nome': employee.nome,
                    'cpf': employee.cpf,
                    'cargo': employee.cargo,
                    'salario': employee.salario
                })
        print(f"Dados de funcionários salvos em '{CSV_FILENAME}' com sucesso.")
        time.sleep(1.5)
    except Exception as e:
        print(f"Erro ao salvar dados no CSV: {e}")
        time.sleep(1.5)

# --- Operações CRUD ---
def add_employee():
    """
    Solicita os dados de um novo funcionário e o adiciona à lista.
    """
    print("\n--- Cadastrar Novo Funcionário ---")
    nome = input("Digite o nome completo do funcionário: ").strip()
    if not nome:
        print("Nome não pode ser vazio. Operação cancelada.")
        time.sleep(1.5)
        return

    cpf = input("Digite o CPF do funcionário (apenas números): ").strip()
    if not cpf.isdigit() or len(cpf) != 11:  # Validação básica de CPF
        print("CPF inválido. Deve conter 11 dígitos numéricos. Operação cancelada.")
        time.sleep(2)
        return

    # Verifica por CPF duplicado
    for employee in EMPLOYEES:
        if employee.cpf == cpf:
            print(f"Erro: Um funcionário com o CPF '{cpf}' já está cadastrado. Operação cancelada.")
            time.sleep(2)
            return

    cargo = input("Digite o cargo do funcionário: ").strip()
    if not cargo:
        print("Cargo não pode ser vazio. Operação cancelada.")
        time.sleep(1.5)
        return

    while True:
        salario_str = input("Digite o salário do funcionário (apenas números, use '.' para centavos): ").strip()
        try:
            salario = float(salario_str)
            if salario <= 0:
                print("Salário deve ser um valor positivo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Salário inválido. Digite um número. Tente novamente.")
    
    new_employee = Funcionario(nome, cpf, cargo, salario)
    EMPLOYEES.append(new_employee)
    save_employees_to_csv()
    print(f"Funcionário '{nome}' cadastrado com sucesso!")
    time.sleep(1.5)

def list_employees():
    """
    Lista todos os funcionários cadastrados.
    """
    print("\n--- Lista de Funcionários ---")
    if not EMPLOYEES:
        print("Nenhum funcionário cadastrado ainda.")
        time.sleep(1.5)
        return

    for i, employee in enumerate(EMPLOYEES):
        print(f"\n--- Funcionário {i+1} ---")
        print(employee)
        time.sleep(0.1) # Pequena pausa para melhor leitura
    time.sleep(2)

def update_employee():
    """
    Atualiza os dados de um funcionário existente.
    """
    print("\n--- Atualizar Dados do Funcionário ---")
    cpf_to_update = input("Digite o CPF do funcionário que deseja atualizar: ").strip()

    found_employee = None
    for employee in EMPLOYEES:
        if employee.cpf == cpf_to_update:
            found_employee = employee
            break

    if not found_employee:
        print(f"Funcionário com CPF '{cpf_to_update}' não encontrado.")
        time.sleep(1.5)
        return

    print(f"\nDados atuais do funcionário com CPF '{cpf_to_update}':")
    print(found_employee)

    print("\nDigite os novos dados (deixe em branco para manter o valor atual):")
    new_nome = input(f"Novo nome ({found_employee.nome}): ").strip()
    if new_nome:
        found_employee.nome = new_nome

    new_cargo = input(f"Novo cargo ({found_employee.cargo}): ").strip()
    if new_cargo:
        found_employee.cargo = new_cargo

    while True:
        new_salario_str = input(f"Novo salário ({found_employee.salario:.2f}): ").strip()
        if not new_salario_str: # Usuário deixou em branco
            break
        try:
            new_salario = float(new_salario_str)
            if new_salario <= 0:
                print("Salário deve ser um valor positivo. Tente novamente.")
            else:
                found_employee.salario = new_salario
                break
        except ValueError:
            print("Salário inválido. Digite um número. Tente novamente.")

    save_employees_to_csv()
    print(f"Dados do funcionário com CPF '{cpf_to_update}' atualizados com sucesso!")
    time.sleep(1.5)

def delete_employee():
    """
    Remove um funcionário da lista.
    """
    print("\n--- Excluir Funcionário ---")
    cpf_to_delete = input("Digite o CPF do funcionário que deseja excluir: ").strip()

    original_len = len(EMPLOYEES)
    EMPLOYEES[:] = [employee for employee in EMPLOYEES if employee.cpf != cpf_to_delete]

    if len(EMPLOYEES) < original_len:
        save_employees_to_csv()
        print(f"Funcionário com CPF '{cpf_to_delete}' excluído com sucesso!")
    else:
        print(f"Funcionário com CPF '{cpf_to_delete}' não encontrado.")
    time.sleep(1.5)

# --- Main Menu and Application Flow ---
def main_menu():
    """
    Exibe o menu principal e gerencia as opções do usuário.
    """
    load_employees_from_csv() # Carrega os dados ao iniciar o programa

    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela
        print("="*40)
        print("   SISTEMA DE GERENCIAMENTO DE FUNCIONÁRIOS")
        print("             DENDÊ TECH")
        print("="*40)
        print("\nEscolha uma opção:")
        print("1. Cadastrar Funcionário")
        print("2. Listar Funcionários")
        print("3. Atualizar Funcionário")
        print("4. Excluir Funcionário")
        print("5. Sair")
        print("="*40)

        choice = input("Digite o número da opção desejada: ").strip()

        if choice == '1':
            add_employee()
        elif choice == '2':
            list_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            print("Saindo do sistema. Até mais!")
            time.sleep(1.5)
            break
        else:
            print("Opção inválida. Por favor, digite um número de 1 a 5.")
            time.sleep(2)

if __name__ == "__main__":
    main_menu()