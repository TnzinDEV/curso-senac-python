class Roupas:
    def __init__(self, tipo, cor):
        self.tipo = tipo
        self.cor = cor


    def vestir(self):
        return f' {self.cor} esta Cor combinou perfeitamente.'


roupa1 = Roupas("camisa","branca")
roupa2 = Roupas("blusa", "lilas")

print(f"sua {roupa1.tipo} e bonita com a cor {roupa1.cor}")
print(roupa1.vestir())