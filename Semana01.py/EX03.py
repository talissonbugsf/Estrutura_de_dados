class Produto:
    def __init__(self, nome, preco, qntd_estoque):
        self.nome = nome
        self.preco = preco
        self.qntd_estoque = qntd_estoque

    def atualizar_estoque(self, qntd_add):
        self.qntd_estoque += qntd_add

    def mostrar_resultados(self):
        print(f"Quantidade atual em estoque:{self.qntd_estoque}")

alguma_coisa = Produto("Alguma", 100, 8)
alguma_coisa.mostrar_resultados()
alguma_coisa.atualizar_estoque(20)
alguma_coisa.mostrar_resultados()
