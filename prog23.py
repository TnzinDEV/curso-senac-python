dia = input("Digite o dia da Semana: ")
match dia:
    case "Segunda" | "Terça" | "Quarta" | "Quinta" | "Sexta" :
        print("Dia de semana. Dia de programar!")
    case "Sabado" | "Domingo" :
        print("Fim de semana! Vai dormir kkkk.")
    case _:
        print("Dia Invalido.")