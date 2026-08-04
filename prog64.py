class passarinhos:
    def __init__(self, raça, cor):
        self.cor = cor
        self.raça = raça
    

    def cantar(self):
        return f"{self.raça} canta."


passarinho1 = passarinhos("bem-te-vi", "verde")
passarinho2 = passarinhos("quero-quero", "amarelo")


print(f"o passarinho {passarinho1.cor} esta cantando")
print(f"o passarinho {passarinho2.raça} esta voando")