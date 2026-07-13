
print("o professor leandro perguntou quem tem mas aura da turma")
print("e logo em seguida abriu uma votaçao por meio de numeros")
print("digite o numero 1 para votar no tony")
print("digite o numero 2 para votar no joao")
print("digite o numero 3 para votar no breno")
print("digite o numero 4 para votar no gustavo")
voto = int(input("escolha em quem votar: "))
if voto == 4:
    print(f"seu voto foi adicionado ao candidato: gustavo")
elif voto == 1:
    print(f"seu voto foi adicionado ao candidato: tony")
elif voto == 2:
    print(f"seu voto foi adicionado ao candidato: joao")
elif voto == 3:
    print(f"seu voto foi adicionado ao candidato: breno")
else:
    print("este candidato nao esta disponivel")