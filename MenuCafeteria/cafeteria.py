def menu():
    """Função para decisão de qual função será executada"""
    print("----------------")
    print(" Menu Cafeteria ")
    print("----------------") #estetica
    print("1. Adicionar item")
    print("2. Excluir item")
    print("3. Alterar item")
    print("4. Buscar item")
    print("5. Cardápio Completo")
    print("6. Cardápio em arquivo texto")
    print("7. Adicionar itens ao carrinho")
    print("8. Sair")

def adicionar(cardapio):
    """Função para adicionar itens no cardapio"""
    print(f"Itens ja existentes: {cardapio}")
    nome = input("Qual item deseja adicionar? ")
    preco = float(input("Qual será o preço do item? "))
    cardapio[nome] = preco
    print(f"O item '{nome}' foi adicionado ao menu.")

def excluir(cardapio):
    """Função para excluir itens do cardapio"""
    print(cardapio)
    ne = input("Qual item deseja excluir? ") #ne = nome excluir
    if ne in cardapio:
        del cardapio[ne]
        print(f"O item '{ne}' foi excluído do cardápio.")
    else:
        print(f"O item '{ne}' não está no cardapio.")

def alterar(cardapio):
    """Função para alterar itens do cardapio"""
    print(cardapio)
    na = input("Qual item deseja alterar? ") #na = nome alterar
    if na in cardapio:
        preco = float(input("Digite o novo preço:  "))
        cardapio[na] = preco
        print(f"O item '{na}' foi alterado.")
    else:
        print(f"O item '{na}' não está no cardápio.")

def buscar(cardapio):
    """Função para buscar itens no cardápio"""
    nb = input("Qual item deseja buscar? ") #nb = nome buscar
    if nb in cardapio:
        print(f"Item: {nb}  Preço: R${cardapio[nb]:.2f}")
    else:
        print(f"Item '{nb}' não está no cardápio.")

def menu_completo(cardapio):
    """Função para mostrar o menu completo"""
    if cardapio:
        print("\nCardápio:")
        for nome, preco in cardapio.items():
            print(f"Item: {nome}, Preço: R${preco:.2f}")
    else:
        print("Cardapio vazio.")

def arquivo(cardapio, nome_arquivo="cardapio.txt"):
    with open(nome_arquivo, "w") as arquivo:
        for nome, preco in cardapio.items():
            arquivo.write(f"{nome}  -  R${preco}\n")
    print(f"Cardápio salvo no arquivo '{nome_arquivo}'.")

def pagar(cardapio):
    total = 0.0
    print(cardapio)
    while True:
        itens = input("Qual item deseja adicionar ao carrinho? ('sair' para encerrar) ")
        if itens == 'sair':
           break
        elif itens in cardapio:
            total += cardapio[itens]
            print(f"item '{itens}' adicionado ao carrinho. Total até agora: R${total}")
        else:
            print(f"o item '{itens}' não esta no cardapio.")
        
    print(f"O total a ser pago é de R${total}")


def escolha():
    """Função que torna o cardápio interativo"""
    cardapio = {}
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar(cardapio)
        elif opcao == "2":
            excluir(cardapio)
        elif opcao == "3":
            alterar(cardapio)
        elif opcao == "4":
            buscar(cardapio)
        elif opcao == "5":
            menu_completo(cardapio)
        elif opcao == "6":
            arquivo(cardapio)
        elif opcao == "7":
            pagar(cardapio)
        elif opcao == "8":
            print("saindo")
            break
        else:
            print("Digite um número de 1 até 8.")

escolha()
