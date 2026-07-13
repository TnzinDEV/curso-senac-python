print("seja bem vindo ao tech park!")
i = int(input("me informe sua idade: "))
ig = input("Voce possui ingresso? responda com (S = sim / N = nao) : ").upper()
if i >= 12 and ig == "S":
    print("acesso liberado!")
elif i < 12 :
    print("acesso negado. [voce nao possui a idade requisitada]")
else:
    print("acesso negado!")
