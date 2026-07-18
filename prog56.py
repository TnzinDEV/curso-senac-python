lista = []
while True:
    produtos = input("Digite o produto que voce quer adicionar ou digite [sair] para sair: ")
    print("-"* 60)
    if produtos == "sair":
        break
    lista.append(produtos)
    print("-"* 60)
    print(f"{produtos} Adicionado ao Carrinho.")
    print("-"* 60)