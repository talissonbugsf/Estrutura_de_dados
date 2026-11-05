class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    #Inserir na cabeça
    def inserir_cabeca(self, dado):
        novo = No(dado)

        if self.head == None:
            self.head = self.tail = novo
            return

        novo.proximo = self.head
        self.head.anterior = novo
        self.head = novo

    def inserir_cauda(self, dado):
        novo = No(dado)

        if self.tail == None:
            self.tail = self.head = novo
            return

        novo.anterior = self.tail
        self.tail.proximo = novo
        self.tail = novo

    def remover_cabeca(self):
        if self.head == None:
            print("Sem viajantes no momento!")
            return
        elif self.head == self.tail:
            self.head = self.tail = None
            print(f"Viajante {self.dado} enviado a missão!")
            return 
        self.head = self.head.proximo
        self.head.anterior = None
        print(f"Viajante {self.dado} enviado a missão!")

    def remover_cauda(self):
        if self.head == None:
            print("Sem viajantes no momento!")
            return
        elif self.head == self.tail:
            self.head = self.tail = None
            print(f"Viajante {self.dado} enviado a missão!")
            return
        self.tail = self.tail.anterior
        self.tail.proximo = None
        print(f"Viajante {self.dado} enviado a missão!")

    def mostrar_cabeca(self):
        if self.head == None:
            print("Sem viajantes no momento!")
            return
        aux = self.head
        while aux != None:
            print(f"- {aux.dado};")
            aux = aux.proximo

    def mostrar_cauda(self):
        if self.tail == None:
            print("Sem viajantes no momento!")
            return
        aux = self.tail
        while aux != None:
            print(f"- {aux.dado};")
            aux = aux.anterior


def menu():
    print("1 - Adicionar viajante no inicio da fila")
    print("2 - Adicionar no final")
    print("3 - Enviar para a missão do inicio")
    print("4 - Enviar do fim")
    print("5 - Mostrar deque pela cabeça")
    print("6 - Sair\n")

    opc = int(input("Digite uma opção:"))
    return opc

def main():
    opc = 0
    deque = Deque()

    while opc != 7:
        opc = menu()

        if opc == 1:
            dado = input("Digite um nome:")
            deque.inserir_cabeca(dado)

        elif opc == 2:
            dado = input("Digite um nome:")
            deque.inserir_cauda(dado)

        elif opc == 3:
            deque.remover_cabeca()

        elif opc == 4:
            deque.remover_cauda()

        elif opc == 5:
            deque.mostrar_cabeca()

        elif opc == 6:
            print("Operações finalizadas!")

        else:
            print("Tente novamente!")

main()
