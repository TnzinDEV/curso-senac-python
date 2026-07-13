print("seu nome: [digite | sair | para sair]: ")
n = ""
while n != "SAIR":
    n = input(f"digite seu nome: ").upper()
    if n=="SAIR":
        break
    print(f"{n}")