class biscoito:
    def __init__(self, sabor, gosto):
        self.sabor = sabor
        self.gosto = gosto

    def croc(self):
        return f'o {self.sabor} faz CROC CROC'
biscoito1= biscoito("energetico", "merda")

print(f"o biscoito saBOR {biscoito1.croc()} ")