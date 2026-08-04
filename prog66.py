while True:
    try:
        numero = int(input("digite um numero inteiro para saber a metade: "))
        metade = numero / 2

        print(f"A metade de {numero} e {metade}")
        break


    except ValueError:
        print("Erro: Voce digitou letras, Por favor, digite um numero inteiro!")