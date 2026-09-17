class No:
    def __init__(self, nome, gols):
        self.nome = nome
        self.gols = gols
        self.proximo = None

def adicionar_inicio(lista, dado, gols):
    novo = No(dado, gols)

    if lista is None:
        lista = novo
        return lista

    novo.proximo = lista
    lista = novo
    return lista

def adicionar_final(lista, dado, gols):
    novo = No(dado, gols)

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

def calcular(lista):
    if lista is None:
        print("Lista vazia!")
        return

    aux = lista
    contador = 0
    soma = 0
    while aux is not None:
        contador += 1
        soma += aux.gols
        aux = aux.proximo

    media = soma / contador 
    print(f"Média de gols marcados:{media}")

def menu():
    print("\nMENU:")
    print("1 - Inserir ao início.")
    print("2 - Inserir ao final")
    print("3 - Percorrer.")
    print("4 - Calular Média")
    print("5 - Sair.")

    opc = int(input("Digite uma opção:"))
    return opc

def main():
    opc = 0
    lista = None
    while opc != 5:
        try:
            opc = menu()
            if opc == 1:
                dado = input("Digite seu nome:").title()
                gols = int(input("Digite a quantidade de gols marcados:"))
                lista = adicionar_inicio(lista, dado, gols)
            elif opc == 2:
                dado = input("Digite seu nome:").title()
                gols = int(input("Digite a quantidade de gols marcados:"))
                lista = adicionar_final(lista, dado, gols)
            elif opc == 3:
                percorrer(lista)
            elif opc == 4:
                calcular(lista)
            elif opc == 5:
                print("Até mais!")
            else:
                print("Tenta denovo!")
        except ValueError:
            print("Digita certo...")

main()
