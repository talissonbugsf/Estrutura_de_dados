class No:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.fim = None

def adicionar_inicio(lista, dado):
    novo = No(dado)

    if lista is None:
        lista = novo
        lista.fim = novo
        return lista

    novo.proximo = lista
    lista = novo
    return lista

def adicionar_final(lista, dado):
    novo = No(dado)

    if lista is None:
        lista = novo
        return lista

    aux = lista
    while aux.proximo is not None:
        aux = aux.proximo
    aux.proximo = novo
    return lista
    
def percorrer(lista):
    if lista is None:
        print("Lista vazia!")
        return
    aux = lista
    contador = 1
    while aux is not None:
        print(f"{contador} - {aux.nome};")
        contador += 1
        aux = aux.proximo

def menu():
    print("\nMENU:")
    print("1 - Inserir ao início.")
    print("2 - Inserir ao final")
    print("3 - Percorrer.")
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
                dado = input("Digite seu nome:").title()
                lista = adicionar_inicio(lista, dado)
            elif opc == 2:
                dado = input("Digite seu nome:").title()
                lista = adicionar_final(lista, dado)
            elif opc == 3:
                percorrer(lista)
            elif opc == 4:
                print("Até mais!")
            else:
                print("Tenta denovo!")
        except ValueError:
            print("Digita certo...")

main()
