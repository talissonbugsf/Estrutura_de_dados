class No:
    def __init__(self, chamado):
        self.chamado = chamado
        self.proximo = None
        self.anterior = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def adicionar_final(self, chamado):
        novo = No(chamado)
        
        if self.tail == None:
            self.tail = self.head = novo
            return
        
        novo.anterior = self.tail
        self.tail.proximo = novo
        self.tail = novo

    def adicionar_inicio(self, chamado):
        novo = No(chamado)

        if self.head == None:
            self.head = self.tail = novo
            return

        novo.proximo = self.head
        self.head.anterior = novo
        self.head = novo        

    def atender(self):
        if self.head == None:
            print("Deque vazio!")
            return
        elif self.head == self.tail:
            self.head = self.tail = None
            return 
        self.head = self.head.proximo
        self.head.anterior = None           

    def listar(self):
        if self.head == None:
            print("Deque vazio!")
            return
        aux = self.head
        while aux != None:
            print(f"- {aux.chamado};")
            aux = aux.proximo

def menu():
    print("MENU:")
    print("1 - Adicionar cliente comum;")
    print("2 - Adicionar cliente preferencial;")
    print("3 - Atender cliente;")
    print("4 - Listar fila;")
    print("5 - Sair.\n")
    opc = int(input("Digite uma opção:"))
    return opc

def main():
    opc = 0
    deque = Deque()
    while opc != 5:
        try:
            opc = menu()
            if opc == 1:
                cliente = input("Digite seu nome:")
                deque.adicionar_final(cliente)

            elif opc == 2:
                cliente = input("Digite seu nome:")
                deque.adicionar_inicio(cliente)

            elif opc == 3:
                deque.atender()

            elif opc == 4:
                deque.listar()

            elif opc == 5:
                print("Até mais!")

            else:
                print("Erro, tenta denovo!")

        except ValueError:
            print("Tenta denovo!")

main()
