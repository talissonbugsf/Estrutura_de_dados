class No:
    def __init__(self, nome, identificador):
        self.nome = nome
        self.identificador = identificador
        self.proximo = None
        self.anterior = None

class ListaDuplaEnca:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir(self, nome, identificador):
        novo = No(nome, identificador)
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            novo.anterior = self.fim
            self.fim = novo
        print(f"Nome {nome} adicionado ao sistema com a identificação {identificador}.")

    def listar(self):
        if self.inicio is None:
            print("Sem nomes e/ou identificação.")
            return
        print("Lista de nomes e identificações:")
        aux = self.inicio
        while aux is not None:
            print(f"Nome: {aux.nome}, Identificador: {aux.identificador}.")
            aux = aux.proximo

    def remover(self, identificador):
        if self.inicio is None:
            print("Sem nomes e/ou identificações.")
            return

        aux = self.inicio
        while aux is not None and aux.identificador != identificador:
            aux = aux.proximo

        if aux is None:
            print(f"Código de identificação {identificador} não encontrado.")
            return
        
        if aux == self.inicio and aux == self.fim:
            self.inicio = None
            self.fim = None
        elif aux == self.inicio:
            self.inicio = aux.proximo
            self.inicio.anterior = None
        elif aux == self.fim:
            self.fim = aux.anterior
            self.fim.proximo = None
        else:
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

    def verificacao_nome(self, nome):
        if self.inicio is None:
            print("Sem nomes na lista.")
            return
        
        aux = self.inicio
        encontrado = False
        while aux != None:
            if aux.nome.upper() == nome.upper():
                print(f"Encontramos seu nome: {aux.nome}")
                encontrado = True
            aux = aux.proximo
        if not encontrado:
            print(f"Nome {nome}, não encontrado.")

    def verificacao_id(self, identificador):
        if self.inicio is None:
            print("Sem identificadores na lista.")
            return
        
        aux = self.inicio
        encontrado = False
        while aux != None:
            if aux.identificador == identificador:
                print(f"Encontramos o ID {aux.identificador} na lista.")
                encontrado = True
            aux = aux.proximo

        if not encontrado:
            print(f"Não encontramos o ID {identificador} na lista.")

def menu():
    print("MENU:")
    print("1 - Inserir no.")
    print("2 - Listar no's.")
    print("3 - Remover no's.")
    print("4 - Verificar se no existe.")
    print("5 - Sair.")

    opc = int(input("\nDigite uma opção:"))
    return opc

def main():
    lista = ListaDuplaEnca()
    opc = 0
    while opc != 5:
        opc = menu()

        if opc == 1:
            nome = input("Digite um nome:").upper()
            identificador = int(input("Digite o código de identificação:"))
            lista.inserir(nome, identificador)
        elif opc == 2:
            lista.listar()
        elif opc == 3:
            identificador = int(input("Digite um código de identificação para remover:"))
            lista.remover(identificador)
        elif opc == 4:
            n_or_id = int(input("Deseja verificar pelo nome(1) ou identificador(2)?"))
            if n_or_id == 1:
                nome = input("Digite o nome para a busca:").upper()
                lista.verificacao_nome(nome)
            elif n_or_id == 2:
                identificador = int(input("Digite o código de identificação para a busca:"))
                lista.verificacao_id(identificador)
            else:
                print("Tente novamente uma opção válida!")
        elif opc == 5:
            print("Até mais bixo véio!\n")
        else:
            print("Digite outra opção, esta é inválida!")

main()
