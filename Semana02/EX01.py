class Produto:
    def __init__(self, nome, preco, qntd_estoque):
        self.nome = nome
        self.preco = preco
        self.qntd_estoque = qntd_estoque

    def exibir(self):
        print(f"Informações do Produto:{self.nome}")
        print(f"Preço: R${self.preco}")
        print(f"Quantidade em estoque:{self.qntd_estoque}")

    def add_estoque(self):
        qntd_adicionar = int(input("Quantos itens deseja adicionar ao estoque:"))
        if qntd_adicionar >= 1:
                self.qntd_estoque += qntd_adicionar
                print(f"Quantidade de itens {qntd_adicionar}, adicionada com sucesso!")
        else:
            print("Erro no processo, tente novamente.")

    def realizar_venda(self):
        venda = int(input("Digite a quantidade de itens que irá vender:"))
        if venda <= self.qntd_estoque:
            self.qntd_estoque -= venda
            print(f"Venda {venda}, realizada com sucesso!")
            print(f"Quantidade atual em estoque do produto {self.nome}:{self.qntd_estoque}")
        else:
            print("Tente novamente.")

    def calcular(self):
        valor_em_estoque = self.qntd_estoque * self.preco
        print(f"Valor em estoque do produto {self.nome}:{valor_em_estoque}")

qntd_ini_ba = int(input("Digite a quantidade inicial de bananas:"))
qntd_ini_ma = int(input("Digite a quantidade inicial de maçãs:"))
qntd_ini_pe = int(input("Digite a quantidade inicial de pêssegos:"))

banana = Produto("Banana", 5, qntd_ini_ba)
maca = Produto("Maçã", 6, qntd_ini_ma)
pessego = Produto("Pêssego", 8, qntd_ini_pe)

menu = 0
while menu != 4:
    menu = int(input("MENU: Selecione 1 para bananas, 2 para maçãs, 3 para pêssegos e 4 para sair do sistema:"))
    if menu == 1:
        select = int(input("Selecione uma opção do menu(1:exibir as informações do produto, 2:Adicionar uma quantidade ao estoque, 3:Realizar uma venda, 4:Calcular o valor em estoque):"))
        if select == 1:
            banana.exibir()
        elif select == 2:
            banana.add_estoque()
        elif select == 3:
            banana.realizar_venda()
        elif select == 4:
            banana.calcular()
        else:
            print("Erro, tente novamente!")

    elif menu == 2:
        select = int(input("Selecione uma opção do menu(1:exibir as informações do produto, 2:Adicionar uma quantidade ao estoque, 3:Realizar uma venda, 4:Calcular o valor em estoque):"))
        if select == 1:
            maca.exibir()
        elif select == 2:
            maca.add_estoque()
        elif select == 3:
            maca.realizar_venda()
        elif select == 4:
            maca.calcular()
        else:
            print("Erro, tente novamente!")  

    elif menu == 3:
        select = int(input("Selecione uma opção do menu(1:exibir as informações do produto, 2:Adicionar uma quantidade ao estoque, 3:Realizar uma venda, 4:Calcular o valor em estoque):"))
        if select == 1:
            pessego.exibir()
        elif select == 2:
            pessego.add_estoque()
        elif select == 3:
            pessego.realizar_venda()
        elif select == 4:
            pessego.calcular()
        else:
            print("Erro, tente novamente!") 

    else:
        print("Até mais!!!")
