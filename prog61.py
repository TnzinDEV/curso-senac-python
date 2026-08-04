class Carros:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def buzinar(self):
        return f"{self.modelo} faz bibi"

carro1 = Carros("toyota", "corola")
carro2 = Carros("vw", "gol")

print(f"A marca do seu Carro e {carro1.marca} e o modelo e {carro1.modelo}")

print(carro1.buzinar())