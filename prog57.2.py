curso = ["Python", "Java"]

print("Cursos disponíveis:")
for item in curso:
    print(f"- {item}")

print("-" * 60)

x = input("Inclua um curso na lista: ")
curso.append(x)

print("-" * 60)
print("Lista atualizada:")
for item in curso:
    print(f"- {item}")

print("-" * 60)

y = input("Digite o curso que você quer remover da lista: ")

if y in curso:
    curso.remove(y)
    print("-" * 60)
    print("Lista após a remoção:")
    for item in curso:
        print(f"- {item}")
else:
    print("Esse curso não está na lista.")