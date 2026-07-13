opcao = int(input("digite uma opçao: "))

match opcao:
    case 1:
        print("voce escolheu a opçao 1: ver saldo. ")
    case 2:
        print("voce escolheua opçao 2: fazer saque. ")
    case 3:
        print("voce escolheu a opçao 3: falar com atendente. ")
    case _:
        print("opçao invalida")