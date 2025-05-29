# Definindo constantes para dedução por dependente no IRRF e valor do plano de saúde
DEDUCAO_DEPENDENTE_IRRF = 189.59
VALOR_PLANO_SAUDE_POR_DEPENDENTE = 150.00

# Credenciais fixas para simulação de login
MATRICULA_VALIDA = "12345"
SENHA_VALIDA = "senha123"

def format_currency(value: float) -> str:
    """Formata um valor float para o padrão monetário brasileiro R$ X.XXX,XX."""
    s = "{:_.2f}".format(value)  # Ex: 12345.67 -> "12_345.67"
    s = s.replace('.', '#')      # -> "12_345#67" (temporário)
    s = s.replace('_', '.')      # -> "12.345#67"
    return f"R$ {s}"

def calcular_inss(salario_base: float) -> float:
    """Calcula o desconto do INSS."""
    # Teto de contribuição e desconto máximo
    TETO_SALARIAL_INSS = 8157.41
    DESCONTO_MAXIMO_INSS = 1142.04 # Conforme especificado que este é o desconto máximo

    if salario_base > TETO_SALARIAL_INSS:
        return DESCONTO_MAXIMO_INSS

    if salario_base <= 1518.00:
        desconto_inss = salario_base * 0.075
    elif salario_base <= 2793.88: # De R$ 1.518,01 até R$ 2.793,88
        desconto_inss = (salario_base * 0.09) - 113.85
    elif salario_base <= 4190.83: # De R$ 2.793,89 até R$ 4.190,83
        desconto_inss = (salario_base * 0.12) - 189.54
    elif salario_base <= TETO_SALARIAL_INSS: # De R$ 4.190,84 até R$ 8.157,41
        desconto_inss = (salario_base * 0.14) - 318.38
    else: # Acima do teto, já tratado no início
        desconto_inss = DESCONTO_MAXIMO_INSS
        
    return round(desconto_inss, 2)

def calcular_irrf(salario_base: float, desconto_inss: float, num_dependentes: int) -> float:
    """Calcula o desconto do IRRF."""
    deducao_total_dependentes = num_dependentes * DEDUCAO_DEPENDENTE_IRRF
    base_calculo_irrf = salario_base - desconto_inss - deducao_total_dependentes

    if base_calculo_irrf <= 2259.20:
        desconto_irrf = 0.0
    elif base_calculo_irrf <= 2826.65: # De 2.259,21 até 2.826,65
        desconto_irrf = (base_calculo_irrf * 0.075) - 169.44
    elif base_calculo_irrf <= 3751.05: # De 2.826,66 até 3.751,05
        desconto_irrf = (base_calculo_irrf * 0.15) - 381.44
    elif base_calculo_irrf <= 4664.68: # De 3.751,06 até 4.664,68
        desconto_irrf = (base_calculo_irrf * 0.225) - 662.77
    else: # Acima de 4.664,68
        desconto_irrf = (base_calculo_irrf * 0.275) - 896.00
        
    return round(max(0, desconto_irrf), 2) # Garante que não seja negativo

def calcular_desconto_vale_transporte(salario_base: float, opta_vt: str) -> float:
    """Calcula o desconto do Vale Transporte."""
    if opta_vt.lower() == 's':
        return round(salario_base * 0.06, 2)
    return 0.0

def calcular_desconto_vale_refeicao(valor_vr_fornecido: float) -> float:
    """Calcula o desconto do Vale Refeição."""
    if valor_vr_fornecido > 0:
        return round(valor_vr_fornecido * 0.20, 2)
    return 0.0

def calcular_desconto_plano_saude(num_dependentes: int) -> float:
    """Calcula o desconto do Plano de Saúde."""
    return round(num_dependentes * VALOR_PLANO_SAUDE_POR_DEPENDENTE, 2)

def autenticar_funcionario() -> bool:
    """Solicita matrícula e senha e verifica as credenciais."""
    print("--- Autenticação da Folha de Pagamento ---")
    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")
    if matricula == MATRICULA_VALIDA and senha == SENHA_VALIDA:
        print("Autenticação bem-sucedida!\n")
        return True
    else:
        print("Matrícula ou senha inválida. Acesso negado.")
        return False

def main():
    """Função principal para executar o sistema de folha de pagamento."""
    if not autenticar_funcionario():
        return

    print("--- Cálculo da Folha de Pagamento ---")
    
    while True:
        try:
            salario_base = float(input("Digite o salário base do funcionário (R$): ").replace(',', '.'))
            if salario_base < 0:
                print("Salário base não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Valor inválido para salário base. Use números.")

    opta_vt = ''
    while opta_vt.lower() not in ['s', 'n']:
        opta_vt = input("Deseja receber vale transporte (s/n)? ").strip()
        if opta_vt.lower() not in ['s', 'n']:
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")

    while True:
        try:
            valor_vr_fornecido = float(input("Digite o valor do vale refeição fornecido pela empresa (R$): ").replace(',', '.'))
            if valor_vr_fornecido < 0:
                print("Valor do vale refeição não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Valor inválido para vale refeição. Use números.")

    while True:
        try:
            num_dependentes = int(input("Digite a quantidade de dependentes: "))
            if num_dependentes < 0:
                print("Número de dependentes não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Valor inválido para quantidade de dependentes. Use um número inteiro.")

    # Cálculos
    desconto_inss = calcular_inss(salario_base)
    desconto_irrf = calcular_irrf(salario_base, desconto_inss, num_dependentes)
    desconto_vt = calcular_desconto_vale_transporte(salario_base, opta_vt)
    desconto_vr = calcular_desconto_vale_refeicao(valor_vr_fornecido)
    desconto_ps = calcular_desconto_plano_saude(num_dependentes)

    total_descontos = desconto_inss + desconto_irrf + desconto_vt + desconto_vr + desconto_ps
    salario_liquido = salario_base - total_descontos

    # Exibição dos resultados
    print("\n--- Holerite ---")
    print(f"Salário Base:                           {format_currency(salario_base)}")
    print("--- Descontos ---")
    print(f"  (-) INSS:                             {format_currency(desconto_inss)}")
    print(f"  (-) IRRF:                             {format_currency(desconto_irrf)}")
    print(f"  (-) Vale Transporte:                  {format_currency(desconto_vt)}")
    print(f"  (-) Vale Refeição:                    {format_currency(desconto_vr)}")
    print(f"  (-) Plano de Saúde (Dependentes):     {format_currency(desconto_ps)}")
    print("-------------------------------------------")
    print(f"Total de Descontos:                   {format_currency(total_descontos)}")
    print("-------------------------------------------")
    print(f"Salário Líquido:                        {format_currency(salario_liquido)}")
    print("-------------------------------------------")

if __name__ == "__main__":
    main()
