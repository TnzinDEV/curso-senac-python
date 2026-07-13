l = input("digite o seu cargo: [C] = Caixa [V] = Vendedor [G] = Gerente : ").upper()
if l =="C":
    print("seu salario e de 1500")
elif l =="V":
    print("seu salario e de 2400")
elif l =="G":
    print("seu salario e de 4000")
else:
    print("seu cargo nao consta no sistema!")
s = int(input("verifique o numero do seu salario: "))




inss = s * 0.12

irrf1 = s * 0.14

irrf2 = s * 0.08




#inss = 12%
if s >= 2000:
    r = s - irrf1 - inss
    print(f"seu salario e de {r : .2f}")
elif s < 2000:
    r = s - irrf2 - inss
    print(f"seu salario e de {r : .2f}")