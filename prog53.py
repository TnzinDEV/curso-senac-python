nomes=["ana", "marcos", "bruno"]
print(f"Listagem de nomes {nomes}")
print("-"* 60)
n = input(f"Digite seu nome para Cadastrar a lista: ")
nomes.append(n)
print("-"* 60)
print(f"Listagem de nome ATUALIZADA {nomes}")
print("-"* 60)
ne = input("Digite o nome que voce quer excluir da lista: ")
print("-"* 60)
nomes.remove(ne)
print(f"Listagem de nome Atualizada {nomes}")
print("-"* 60)
l = len(nomes)
print(f"A lista em {l} Itens")
print("-"* 60)
#append - incluir

#remove - excluir

#sort - colocar em ordem

#len - contar

#l = len(lista) 
