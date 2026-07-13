t = int(input("digite a temperatura atual: "))
if t > 0 and t < 25:
    print("hoje o clima esta frio!")
elif t >25 and t < 35:
    print("hoje o clime esta agradavel!")
elif t > 35 and t < 50:
    print("hoje o clima esta quente!")
else:
    print("esta temperatura nao consta no meu sistema :-[")
