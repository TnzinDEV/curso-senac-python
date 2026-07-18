def montar_carrinho():
    carrinho = []
    print("=== BEM-VINDO AO SUPERMERCADO PYTHON ===")

    while True:
        produto = input("Digite um produto (ou 'sair' para finalizar): ")

        if produto.lower() == "sair":
            break

        carrinho.append(produto)
        print(f"-> '{produto}' adicionado ao carrinho com sucesso!\n")

    print("\n=== SEU CARRINHO DE COMPRAS ===")

    if not carrinho:
        print("Seu carrinho está vazio.")
    else:
        for item in carrinho:
            print(f"- {item}")

    print(f"\nTotal de itens no carrinho: {len(carrinho)}")


montar_carrinho()