class Duplamente:
    def __init__(self, id, nome, status):
        self.id = id
        self.nome = nome
        self.status = status
        self.proximo = None
        self.anterior = None

def inserir(lista, id, nome, status):
    novo = Duplamente(id, nome, status)

    if lista is None:
        lista = novo
        return lista

    novo.proximo = lista
    lista.anterior = novo
    lista = novo
    return lista

def remover(lista, id):
    if lista is None:
        print("Lista vazia!")
        return lista

    aux = lista
    while aux is not None:
        if id == aux.id:
            if id == lista:
                lista = lista.proximo
                lista.anterior = None
                return lista
            elif aux.anterior == aux.proximo == None:
                lista = None
                return lista
            elif aux.proximo == None:
                aux.anterior.proximo = None
                return lista
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior
            return lista
        aux = aux.proximo
    print(f"{aux.id} não encontrado!")

def ligar_desligar(lista, id):
    if lista is None:
        print("Lista vazia!")
        return
    aux = lista
    while aux is not None:
        if aux.id == id:
            if aux.status == True:
                aux.status = False
                return lista
            elif aux.status == False:
                aux.status = True
                return lista
            aux = aux.proximo
    print(f"{id} não encontrado!")
    return lista

def percorrer_normal(lista):
    if lista is None:
        print("Lista vazia!")
        return 
    aux = lista
    while aux is not None:
        print(f" - {aux.id}, {aux.nome}, {aux.status};")
        aux = aux.proximo

def percorrer_contrario(lista):
    if lista is None:
        print("Lista vazia!")
        return
    aux = lista
    while aux.proximo is not None:
        aux = aux.proximo

    while aux is not None:
        print(f" - {aux.id}, {aux.nome}, {aux.status};")
        aux = aux.anterior

def main():
    lista = None
    lista = inserir(lista, 9874, "Pedro", True)
    lista = inserir(lista, 7149, "Puntel", True)
    lista = inserir(lista, 8243, "Vini", False)
    print("")
    percorrer_normal(lista)
    print("")
    percorrer_contrario(lista)
    id = 9874
    lista = remover(lista, id)
    print("")
    percorrer_normal(lista)
main()
