#uma funçao em python e como uma receita de bolo ou uma maquina que voce deixa guardada para usar sempre que precisa.


#em vem de escrever o mesmo codigo varias vezes, voce o empacota dentro de uma funçao, da um nome a ele e o chamasempre que quiser.


#como funciona? (fluxo em 4 passos)
#definiçao (def): e onde vocecria e da um nome a ela.

#Entrada (Parametros): os "ingredientes" que a maquina precisa para trabalhar (Opicional)

#Processamento: o codigo dentro dela que faz o trabalho pesado.

#saida: (return): O resultado que a maquina te entrega de volta (Opcional)

#a variavel dentro do parentese da [def] sao apenas exemplar.

#*****
#Exp de parametro 

nome = input("Digite seu NickName: ")
def saudaçao(n):
    print(f"{n} Entrou no Game.")
print("...")
print("...")
print("...")
saudaçao(nome)
#exercicio 2 


def user(n, s):
    print(f"Koe {n} {s}. Suave Irmao?!")




nome = input("Digite seu NickName: ")
sobre = input("Digite o seu Sobrenome: ")
print("...")
print("...")
print("...")
user(nome, sobre)

#processamento de calculos

#soma
def somar(v1, v2):
    return v1 + v2

valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite um valor: "))
total = somar(valor1, valor2)
print("...")
print(f"O total e de: {total}")


#Porcentagem

def porcentagem_por_15(valor):
    return valor * 0.15


v1 = int(input("Digite o valor da Compra: "))
print("Sera adicionada uma Taxa de 15%.")
pct = porcentagem_por_15(v1)
m = v1 + pct
print(f"O valor final e de {m: .2f}")

#media

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