for i in range (0,5):
    v = int(input("digite cinco numeros e eu direi se e impar ou par: "))
    y = v % 2
    if y == 0 :
        print(f"O numero {v} e par")
    else:
        print(f"O numero {v} e impar")