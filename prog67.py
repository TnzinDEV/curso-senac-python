def media(n1, n2, n3, n4, ):
    t = (n1 + n2 + n3 + n4) / 4 
    if t >=7:
        print(f"Sua Media e de {t}. Voce foi Aprovado.")
    elif t >= 5:
        print(f"Sua media e de {t}. Voce esta de Recuperaçao.")
    else:
        print(f"Voce foi Reprovado.")

nome = input("Digite o Nome do Aluno: ")
nota1 = float(input("Digite a sua Nota Referente ao Primeiro Bimestre: "))
nota2 = float(input("Digite a sua Nota Referente ao Segundo Bimestre: "))
nota3 = float(input("Digite a sua Nota Referente ao Terceiro Bimestre: "))
nota4 = float(input("Digite a sua Nota Referente ao Quarto Bimestre: "))
print(f"O aluno {nome} ")
media(nota1, nota2, nota3, nota4, )