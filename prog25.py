#'''digite dois numeros e mostra o menu abaixo..

#-- escolha a operaçao--
#1-somar
#2-subtrair
#3-multiplicar
#4-dividir
#'''
v1 = int(input("digite o primeiro valor: "))

v2 = int(input("digite o segundo valor: "))
print("-------tabela de operaçoes-------")
print("+ para somar: ")
print("- para subtrair: ")
print("* para multiplicar: ")
print("/ para dividir")

o = input("digite o operador: ")
r = 0
match o:
    case "+":
         r = v1 + v2
    case "-":
        r = v1 - v2
    case "*":
        r = v1 * v2
    case "/":
        r = v1 / v2
    case _:
    print("Operaçao invalida!")
print(f"O Resultado da sua operaçao e de: {r}")
print("commit test")
print("six seven")
print("breno yag")
