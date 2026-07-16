print("Ola! seja bem vindo a EMBARE KRAFT")
print("-"* 160)
print("Aqui vai uma lista de tamanhos.")
scl = [ "18x24x12", "22x32x12", "22x34x14", "23x39x15" ]
p1 = 1.10
p2 = 1.20
p3 = 1.40
p4 = 1.60
for sc in scl:
    print(f"{sc}")
    print("-"* 160)
t = input("Qual tamanho de sacola voce deseja?: ")
print("-"* 160)
qnt =int(input("Digite a quantidade que voce deseja:"))
print("-"* 160)
q1 = qnt * p1
q2 = qnt * p2
q3 = qnt * p3
q4 = qnt * p4
if t == "18x24x12":
    print(f"Pague o valor a seguir: {q1: .2f}")
    print("-"* 160)
elif t == "22x32x12":
    print(f"Pague o valor a seguir: {q2: .2f}")
    print("-"* 160)
elif t == "22x34x14":
    print(f"Pague o valor a seguir: {q3: .2f}")
    print("-"* 160)
elif t == "23x39x15":
    print(f"Pague o valor a seguir: {q4: .2f}")
    print("-"* 160)
else:
    print("--------Valor invalido ou nao encontrado--------")
print("Para realizar o Pix segue ao Pix abaixo")
print("Pix Exemple")