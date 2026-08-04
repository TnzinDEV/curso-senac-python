try:
    numerador = int(input("Digite o numero a ser dividido: "))
    denominador = int(input("Digite o valor da divisao: "))

    resultado = numerador / denominador
    print(f"O resultado e {resultado: .2f}")

except ValueError:
    print("Digite apenas numeros inteiros.")

except ZeroDivisionError:
    print("Nao e e possivel a divisao por Zero!")