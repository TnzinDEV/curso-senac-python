print("seja bem vindo ao alistamento militar do exercito do rio de janeiro")
m = input("me informe o seu nome: ")
i = int(input("me informe usa idade: "))
s = input("me informe seu genero (M - masculino / F - feminino): ").upper()

if s == "M" and i >= 18:
    print(f"parabens {m}, voce esta apto a se alistar!")
else:
    print(f"desculpe {m}, voce nao esta apto!")