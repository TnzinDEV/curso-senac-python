def porcentagem_por_15(valor):
    return valor * 0.15


v1 = int(input("Digite o valor da Compra: "))
print("Sera adicionada uma Taxa de 15%.")
pct = porcentagem_por_15(v1)
m = v1 + pct
print(f"O valor final e de {m: .2f}")