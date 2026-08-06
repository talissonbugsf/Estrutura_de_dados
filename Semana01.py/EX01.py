class Produto:
    def __init__(self, preco, quantidade):
        self.preco = preco
        self.quantidade = quantidade
    def calcular_total(self):
        resultado = self.quantidade * self.preco
        print(f"Valor final: R$ {resultado}")
coca = Produto(20, 50)
coca.calcular_total()
