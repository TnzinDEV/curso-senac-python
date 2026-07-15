print("---mercadinho do Tn---")
print ("-" * 200)
print("tabela de preços abaixo")
print ("-" * 200)
print("produtos #001 -> Arroz (4.00) | #002 -> Feijao (7.00) | #003 -> Macarrao (5.00)")
print ("-" * 200)
pd = ""
p = 0
while pd != 0:
    pd = int(input("Digite o codigo do produto que deseja: "))
    if pd == 1:
        print("Arroz adicionado. [4.00]")
        print ("-" * 200)
        p = p + 4
    elif pd == 2:
        print("Fejao adicionado. [7.00]")
        print ("-" * 200)
        p = p + 7
    elif pd == 3:
        print("Macarrao adicionado. [5.00]")
        print ("-" * 200)
        p = p + 5
    elif pd == 0:
        print(f"{p}")
        break
else:
        print(f"produto nao encontrado")
        print ("-" * 200)