nm = input("digite seu nome: ")
nt1 = float(input("digite sua nota: "))
nt2 = float(input("digite sua nota: "))
nt3 = float(input("digite sua nota: "))
nt4 = float(input("digite sua nota: "))
m = (nt1+nt2+nt3+nt4)/4
print(f"{nm}, sua media anual e de: {m : .2f}")
if m >= 6.0:
    print("parabens! voce foi aprovado!")
else:
    print("voce esta em recuperaçao!")