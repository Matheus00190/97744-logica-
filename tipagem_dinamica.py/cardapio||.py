# cardapio.py

def obter_cardapio():
    """
    Retorna o cardápio do restaurante com código, nome e preço dos pratos.
    """
    cardapio = {
        1: {"nome": "Feijoada Completa", "preco": 35.00},
        2: {"nome": "Moqueca de Peixe", "preco": 45.00},
        3: {"nome": "Acarajé (3 unidades)", "preco": 20.00},
        4: {"nome": "Xinxim de Galinha", "preco": 38.00},
        5: {"nome": "Vatapá", "preco": 22.00},
        6: {"nome": "Bobó de Camarão", "preco": 40.00},
        7: {"nome": "Caruru", "preco": 25.00}
    }
    return cardapio

def exibir_cardapio(cardapio):
    """
    Exibe o cardápio formatado para o usuário.
    """
    print("\n----- CARDÁPIO DO RESTAURANTE SABORES DA BAHIA -----")
    print("Código | Nome do Prato         | Preço")
    print("-------|-----------------------|--------")
    for codigo, detalhes in cardapio.items():
        print(f"{codigo:<7}| {detalhes['nome']:<21}| R$ {detalhes['preco']:.2f}")
    print("--------------------------------------------------")
    print("Digite '0' para finalizar o pedido a qualquer momento.")

if __name__ == "__main__":
    # Testando as funções iniciais
    menu = obter_cardapio()
    exibir_cardapio(menu)