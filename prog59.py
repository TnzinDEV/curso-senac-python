lista = []
while True:
    x = input("Digite o seu produto [Digite (sair) para sair]: ")
    print("-"* 60)
    if x == "sair":
        break

    else:
        lista.append(x)
        print("-"* 60)
        print(f"{x} Adicionado")
for i in lista:
    print("-"* 60)
    print(i)
