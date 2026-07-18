carro = []
for i in range (3):


    x = input("Cadastre o carro a lista: ")
    print("-"* 60)
    carro.append(x)
    print(f"Adicionado a Lista: {x}")
    print("-"* 60)
print(f"Verifique sua lita Atualizada abaixo.")
i = 0
while i < len(carro):
    print("-"* 60)
    print(carro[i])
    i += 1