print("---Comanda do Garçon---")
print ("-" * 200)
print("DIgite: 001 Para Hamburguer | 002 para Batata Frita | 003 Para Coca-cola")
print ("-" * 200)
print("Digite 000 Para sair")
print ("-" * 200)
pd = ""
t = 0

while pd != "0":
    pd = (input("Digite o codigo do produto: "))
    print ("-" * 200)
    if pd == "1":
        t = t + 25
        print("Hamburguer Adicionado")
        print ("-" * 200)
    elif pd == "2":
        t = t + 10
        print("Batata Frita Adicionada")
        print ("-" * 200)
    elif pd == "3":
        t = t + 11
        print("Coca-Cola Adicionada")
        print ("-" * 200)
    elif pd == "0":
        print(f"Valor sem o adicional de 10% do Garçon e: {t}")
        print ("-" * 200)
    else:
        print("Produto nao encontrado")
        print ("-" * 200)
pdt = t * 1.1
print(f"O Valor final e de : {pdt}")
print ("-" * 200)
print("----encerrando pedido----")
print ("-" * 200)