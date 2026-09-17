class No:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None

def adicionar(lista, dado):
    novo = No(dado)

    if lista is None:
        lista = novo
        return lista

    novo.proximo = lista
    lista = novo
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
    print("1 - Inserir.")
    print("2 - Percorrer.")
    print("3 - Sair.")

    opc = int(input("Digite uma opção:"))
    return opc

def main():
    opc = 0
    lista = None
    while opc != 3:
        try:
            opc = menu()
            if opc == 1:
                dado = input("Digite seu nome:").title()
                lista = adicionar(lista, dado)
            elif opc == 2:
                percorrer(lista)
            elif opc == 3:
                print("Até mais!")
            else:
                print("Tenta denovo!")
        except ValueError:
            print("Digita certo...")

main()
