
import csv
import os
import time

EMPLOYEES = []  # List to store Funcionario objects
CSV_FILENAME = 'funcionarios.csv'

# --- Class Definition ---
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

# --- Data Persistence Functions ---
def load_employees_from_csv():
    """
    Carrega os dados dos funcionários de um arquivo CSV para a lista em memória.
    """
    EMPLOYEES.clear()  # Clear existing data before loading
    if not os.path.exists(CSV_FILENAME):
        print(f"Arquivo '{CSV_FILENAME}' não encontrado. Iniciando com lista vazia.")
        time.sleep(1.5)
        return

    try:
        with open(CSV_FILENAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    # Ensure correct type conversion for salary
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

            writer.writeheader()  # Write the header row
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

# --- CRUD Operations ---
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
    if not cpf.isdigit() or len(cpf) != 11: # Basic CPF validation
        print("CPF inválido. Deve conter 11 dígitos numéricos. Operação cancelada.")
        time.sleep(2)
        return

    # Check for duplicate CPF
    for employee in EMPLOYEES:
        if employee.cpf == cpf:
            print(f"Erro: funcion