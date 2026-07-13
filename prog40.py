c = {}
for cmv in range (2):
    m = input("Marca: ")
    v = float(input("Valor: "))
    c1 = input("Carro: ")
    c[c1] = {
        "marca": m,
        "valor": v
    }
    print(f"Seu carro corresponde ao seguinte cadastro: {c}")