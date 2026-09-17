class NoDuplo:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None

def adicionar(lista, dado):
    novo = NoDuplo(dado)

    if lista is None:
        lista = novo
        return lista

    novo.proximo = lista
    lista.anterior = novo
    lista = novo
    return lista

def percorrer(lista):
    if lista is None:
        print("Lista vazia!")
        return

    contador = 1
    aux = lista
    while aux is not None:
        print(f"{contador} - {aux.nome};")
        contador += 1
        aux = aux.proximo

def percorrer_contrario(lista):
    if lista is None:
        print("Lista vazia!")
        return

    aux = lista

    while aux.proximo is not None:
        aux = aux.proximo

    while aux is not None:
        print(f"{aux.nome};")
        aux = aux.anterior

def menu():
    print("MENU:")
    print("1 - Inserir.")
    print("2 - Percorrer.")
    print("3 - Percorrer ao contrário.")
    print("4 - Sair.")
    opc = int(input("Digite uma opção:"))
    return opc

def main():
    opc = 0
    lista = None

    while opc != 4:
        try:
            opc = menu()
            if opc == 1:
                dado = input("Digite o nome do atleta:")
                lista = adicionar(lista, dado)
            elif opc == 2:
                percorrer(lista)
            elif opc == 3:
                percorrer_contrario(lista)
            elif opc == 4:
                print("Até mais!")
            else:
                print("Tenta denovo!")

        except ValueError:
            print("Digita certo...")

main()
