class No:
    def __init__(self, parada):
        self.parada = parada
        self.proximo = None
        self.anterior = None

def adicionar(lista, parada):
    no = No(parada)

    if lista is None:
            no.proximo = no
            no.anterior = no
            lista = no
            return lista
    
    no.proximo = lista
    no.anterior = lista.anterior
    lista.anterior.proximo = no
    lista.anterior = no
    lista = no
    return lista


def remover(lista, parada):
    if lista is None:
        print("Lista vazia!")
        return
    aux = lista
    while True:
        if aux.parada == parada:
            if aux.proximo == aux:
                print("Único elemento na lista.")
                return None
            elif aux == lista:
                lista.proximo.anterior = lista.anterior
                lista.anterior.proximo = lista.proximo
                lista = lista.proximo
                return lista
            else:
                aux.proximo.anterior = aux.anterior
                aux.anterior.proximo = aux.proximo
                return lista

        elif aux.proximo == lista: 
            print("Dado não encontrado!")
            return lista
        aux = aux.proximo


def listar(lista):
    if lista is None:
        print("Lista vazia!")
        return
    aux = lista
    while True:
        print(f"Parada: {aux.parada}.")
    
        if aux.proximo == lista:
            return
        aux = aux.proximo

    

def menu():
    print("\nPARADAS DE ÔNIBUS:")
    print("1 - Adicionar parada.")
    print("2 - Remover parada.")
    print("3 - Simular percurso.")
    print("4 - Sair.")
    opc = int(input("\nDigite uma opção:"))
    return opc

def main():
    lista = None
    opc = 0

    while opc != 4:
        opc = menu()

        if opc == 1:
            parada = int(input("Digite um id da parada:"))
            lista = adicionar(lista, parada)

        elif opc == 2:
            parada = int(input("Digite um id para remoção:"))
            lista = remover(lista, parada)

        elif opc == 3:
            listar(lista)

        elif opc == 4:
            print("Valeuuu!")

        else:
            print("Tenta denovo!")

main()
