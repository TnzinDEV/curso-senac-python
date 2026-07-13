for i in range (4):
    n = input("Digite o nome do aluno: ")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a primeira nota: "))
    n3 = float(input("Digite a primeira nota: "))
    m = (n1+n2+n3) /3
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------------------------")
    if  m >= 7:
         print(f"o aluno {n} tirou as seguintes notas: {n1} | {n2} | {n3} logo sua media foi{m} seu status atual e de aprovado :-]")
    elif m <= 6 or m >= 5:
        print(f"o aluno {n} tirou as seguintes notas: {n1} | {n2} | {n3} logo sua media foi{m} seu status atual e de recuperaçao :-|")
    else:
        print(f"o aluno {n} tirou as seguintes notas: {n1} | {n2} | {n3} logo sua media foi{m} seu status atual e de reprovado :-[")

        print(f"o aluno {n} tirou as seguintes notas: {n1} | {n2} | {n3} logo sua media foi{m}")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print(" ")