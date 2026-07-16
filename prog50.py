def calculo_nascimento(ano1, anot):
    return anot - ano1




ano_do_nascimento = int(input("Digite o ano do seu nascimento: "))
ano_atual = 2026
idade = calculo_nascimento(ano_do_nascimento, ano_atual)

def maior(i):
    if idade >= 65:
        print(f"Sua idade e de: {idade}anos. Voce e idoso.")
    elif idade >= 18:
        print(f"Sua idade e de: {idade}anos. Voce e maior de idade.")
    else:
        print(f"Sua idade e de: {idade}anos. Voce e menor de idade.")