class No:
    def __init__(self,nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None

def inserir(fila_inicio, fila_fim, nome):
    novo = No(nome)

    if fila_inicio == None:
        fila_inicio = novo
        fila_fim = novo
        return fila_inicio, fila_fim

    fila_fim.proximo = novo
    novo.anterior = fila_fim
    fila_fim = novo
    return fila_inicio, fila_fim

def listar(fila_fim):
    aux = fila_fim
    contador = 1
    if fila_fim == None:
        print("Fila vazia!")
        return
    while aux is not None:
        print(f"{contador} - {aux.nome}")
        contador += 1
        aux = aux.proximo

def remover(fila_inicio, fila_fim):
    if fila_inicio == None:
        print("Fila vazia!")
        return None, None
    if fila_fim == fila_inicio:
        print("Única pessoa na fila.")
        return None, None

    fila_inicio = fila_inicio.proximo
    fila_inicio.anterior = None
    return fila_inicio, fila_fim

def menu():
    print("MENU:")
    print("1 - Inserir pessoa no atendimento.")
    print("2 - Listar pessoas aguardando atendimento.")
    print("3 - Remover pessoa do atendimento.")
    print("4 - Sair.")
    opc = int(input("Digite uma opção:"))
    return opc

def main():
    fila_inicio = None
    fila_fim = None
    opc = 0

    while opc != 4:
        try:
            opc = menu()

            if opc == 1:
                try:
                    nome = input("Digite seu nome:")
                    fila_inicio, fila_fim = inserir(fila_inicio, fila_fim, nome)
                except ValueError:
                    print("Erro ao digitar.")

            elif opc == 2:
                listar(fila_inicio)

            elif opc == 3:
                fila_inicio, fila_fim = remover(fila_inicio, fila_fim)

            elif opc == 4:
                print("Até mais!")

            else:
                print("Tenta denovo!")

        except ValueError:
            print("Erro ao digitar!")

main()
