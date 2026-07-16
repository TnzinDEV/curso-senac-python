def media(n1, n2, n3, n4, ):
    t = (n1 + n2 + n3 + n4) / 4 
    if t >=7:
        print(f"Sua Media e de {t}. Voce foi aprovado.")
    elif t >= 5:
        print(f"Sua media e de {t}. Voce esta de recuperaçao.")
    else:
        print(f"Voce foi reprovado.")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media(nota1, nota2, nota3, nota4, )