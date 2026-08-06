anon = int(input("Digite o Ano do Seu Nascimento: "))
anoa = 2026
anof = anoa - anon

if anof >= 65:
    print("Com base na Tabela Voce esta na Categoria | Idoso |.") 
elif anof >= 18:
    print("Com base na Tabela Voce esta na Categoria | Adulto |.")
elif anof >= 0:
    print("Com base na Tabela Voce esta na Categoria | menor de idade |.") 
else:
    print("Sua Idade nao Consta Na Tabela.")