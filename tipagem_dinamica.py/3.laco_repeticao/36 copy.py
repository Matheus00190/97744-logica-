import os
from dataclasses import dataclass
from typing import List, Optional

# --- Função Auxiliar ---
def limpar_tela():
    """Limpa o console para melhorar a visualização."""
    os.system("cls || clear")

# --- Classe Funcionario ---
@dataclass
class Funcionario:
    """Representa um funcionário com seus dados básicos."""
    nome: str
    cpf: str  # Idealmente, adicione validação de formato e unicidade
    data_nascimento: str  # Considere usar o tipo datetime.date para validação e manipulação
    funcao: str

    def __str__(self):
        """Retorna uma representação em string formatada dos dados do funcionário."""
        return (
            f"Nome: {self.nome}\n"
            f"CPF: {self.cpf}\n"
            f"Data de Nascimento: {self.data_nascimento}\n"
            f"Função: {self.funcao}\n"
        )

# --- Funções de Gerenciamento ---

def verificar_lista_vazia(lista_funcionarios: List[Funcionario]) -> bool:
    """Verifica se a lista de funcionários está vazia e exibe uma mensagem."""
    if not lista_funcionarios:
        print("\nA lista de funcionários está vazia.")
        return True
    return False

def buscar_funcionario_por_nome(lista_funcionarios: List[Funcionario], nome: str) -> Optional[Funcionario]:
    """
    Busca um funcionário pelo nome na lista. Retorna o primeiro encontrado.
    A busca é insensível a maiúsculas/minúsculas.
    """
    # Observação: Se nomes puderem se repetir, buscar por CPF (ou outro ID único) seria mais robusto.
    for funcionario in lista_funcionarios:
        if funcionario.nome.lower() == nome.lower():
            return funcionario
    return None

def adicionar_funcionario(lista_funcionarios: List[Funcionario]):
    """Coleta os dados e adiciona um novo funcionário à lista."""
    limpar_tela()
    print("--- Adicionar Novo Funcionário ---")

    nome = input("Nome: ").strip()
    while not nome: # Validação simples para não permitir nome vazio
        print("O nome não pode ser vazio.")
        nome = input("Nome: ").strip()

    cpf = input("CPF (ex: 123.456.789-00): ").strip()
    # Adicionar validação de formato de CPF aqui (ex: usando regex ou uma biblioteca)
    # Adicionar verificação se o CPF já existe na lista_funcionarios

    data_nascimento = input("Data de Nascimento (ex: DD/MM/AAAA): ").strip()
    # Adicionar validação de formato de data aqui

    funcao = input("Função: ").strip()
    while not funcao: # Validação simples para não permitir função vazia
        print("A função não pode ser vazia.")
        funcao = input("Função: ").strip()

    # Verifica se já existe um funcionário com o mesmo CPF
    for func in lista_funcionarios:
        if func.cpf == cpf:
            print(f"\nErro: Já existe um funcionário cadastrado com o CPF {cpf}.")
            input("Pressione Enter para continuar...")
            return

    novo_funcionario = Funcionario(nome=nome, cpf=cpf, data_nascimento=data_nascimento, funcao=funcao)
    lista_funcionarios.append(novo_funcionario)
    print("\nFuncionário adicionado com sucesso!")
    input("Pressione Enter para continuar...")

def listar_funcionarios(lista_funcionarios: List[Funcionario]):
    """Exibe os dados de todos os funcionários cadastrados."""
    limpar_tela()
    print("--- Lista de Funcionários ---")
    if verificar_lista_vazia(lista_funcionarios):
        input("Pressione Enter para continuar...")
        return

    for i, funcionario in enumerate(lista_funcionarios, 1):
        print(f"--- Funcionário {i} ---")
        print(funcionario) # Utiliza o método __str__ da classe Funcionario
    input("Pressione Enter para continuar...")

def atualizar_funcionario(lista_funcionarios: List[Funcionario]):
    """Permite a atualização dos dados de um funcionário existente."""
    limpar_tela()
    print("--- Atualizar Dados do Funcionário ---")
    if verificar_lista_vazia(lista_funcionarios):
        input("Pressione Enter para continuar...")
        return

    nome_para_atualizar = input("Digite o nome do funcionário que deseja atualizar: ").strip()
    funcionario = buscar_funcionario_por_nome(lista_funcionarios, nome_para_atualizar)

    if funcionario:
        print("\nFuncionário encontrado. Insira os novos dados (deixe em branco para manter o valor atual):")

        novo_nome = input(f"Novo nome (atual: {funcionario.nome}): ").strip()
        if novo_nome:
            funcionario.nome = novo_nome

        novo_cpf = input(f"Novo CPF (atual: {funcionario.cpf}): ").strip()
        if novo_cpf:
            # Importante: Se o CPF for alterado, verificar se o novo CPF já existe!
            cpf_existente = any(f.cpf == novo_cpf and f is not funcionario for f in lista_funcionarios)
            if cpf_existente:
                print(f"Erro: O novo CPF '{novo_cpf}' já está em uso por outro funcionário.")
            else:
                funcionario.cpf = novo_cpf
                print("CPF atualizado.")
        
        nova_data_nascimento = input(f"Nova data de nascimento (atual: {funcionario.data_nascimento}): ").strip()
        if nova_data_nascimento:
            funcionario.data_nascimento = nova_data_nascimento

        nova_funcao = input(f"Nova função (atual: {funcionario.funcao}): ").strip()
        if nova_funcao:
            funcionario.funcao = nova_funcao

        print("\nDados do funcionário atualizados com sucesso!")
    else:
        print(f"\nFuncionário com o nome '{nome_para_atualizar}' não encontrado.")
    input("Pressione Enter para continuar...")

def excluir_funcionario(lista_funcionarios: List[Funcionario]):
    """Remove um funcionário da lista."""
    limpar_tela()
    print("--- Excluir Funcionário ---")
    if verificar_lista_vazia(lista_funcionarios):
        input("Pressione Enter para continuar...")
        return

    nome_para_excluir = input("Digite o nome do funcionário que deseja excluir: ").strip()
    funcionario_para_remover = None
    indice_para_remover = -1

    for i, funcionario in enumerate(lista_funcionarios):
        if funcionario.nome.lower() == nome_para_excluir.lower():
            funcionario_para_remover = funcionario
            indice_para_remover = i
            break # Encontrou o primeiro funcionário com o nome

    if funcionario_para_remover:
        print("\n--- Dados do Funcionário a ser Excluído ---")
        print(funcionario_para_remover)
        confirmacao = input(f"Tem certeza que deseja excluir '{funcionario_para_remover.nome}'? (s/N): ").strip().lower()
        if confirmacao == 's':
            lista_funcionarios.pop(indice_para_remover)
            print("\nFuncionário excluído com sucesso!")
        else:
            print("\nExclusão cancelada.")
    else:
        print(f"\nFuncionário com o nome '{nome_para_excluir}' não encontrado.")
    input("Pressione Enter para continuar...")

# --- Loop Principal e Menu ---
def menu_principal():
    """Exibe o menu principal e gerencia a interação com o usuário."""
    lista_de_funcionarios: List[Funcionario] = []

    # Exemplo de como adicionar funcionários iniciais para teste (opcional)
    # lista_de_funcionarios.append(Funcionario("Alice Wonderland", "111.111.111-11", "10/03/1990", "Engenheira"))
    # lista_de_funcionarios.append(Funcionario("Bob The Builder", "222.222.222-22", "25/07/1985", "Analista"))

    while True:
        limpar_tela()
        print("===== Sistema de Gerenciamento de Funcionários =====")
        print("\nEscolha uma opção:")
        print("1. Adicionar Funcionário")
        print("2. Listar Funcionários")
        print("3. Atualizar Funcionário")
        print("4. Excluir Funcionário")
        print("5. Sair")

        escolha = input("\nDigite o número da opção desejada: ").strip()

        if escolha == '1':
            adicionar_funcionario(lista_de_funcionarios)
        elif escolha == '2':
            listar_funcionarios(lista_de_funcionarios)
        elif escolha == '3':
            atualizar_funcionario(lista_de_funcionarios)
        elif escolha == '4':
            excluir_funcionario(lista_de_funcionarios)
        elif escolha == '5':
            limpar_tela()
            print("Obrigado por utilizar o sistema. Até logo! 👋")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção de 1 a 5.")
            input("Pressione Enter para tentar novamente...")

if __name__ == "__main__":
    menu_principal()