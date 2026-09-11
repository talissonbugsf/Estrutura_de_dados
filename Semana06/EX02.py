class No:
    def __init__(self, operacao):
        self.operacao = operacao
        self.proximo = None

def inserir(pilha, operacao):
    novo = No(operacao)

    if pilha is None:
        pilha = novo
        print(f"Operação {novo.operacao} adicionada a pilha!")
        return pilha

    novo.proximo = pilha
    pilha = novo
    print(f"Operação {novo.operacao} adicionada a pilha!")
    return pilha

def remover(pilha):
    if pilha is None:
        print("Lista vazia!")
        return

    return pilha.proximo

def mostrar_topo(pilha):
    if pilha is None:
        print("Lista vazia!")
        return 

    aux = pilha
    while aux is not None:
        print(f"Última operação inserida: {aux.operacao}")
        break

def mostrar_ope_pendentes(pilha):
    if pilha is None:
        print("Lista vazia!")
        return 
    
    aux = pilha
    while aux is not None:
        print(f"Última operação inserida: {aux.operacao}")
        aux = aux.proximo

def menu():
    print("MENU:")
    print("1 - Inserir operação.")
    print("2 - Remover operação.")
    print("3 - Mostrar a última operação inserida.")
    print("4 - Mostrar operações pendentes.")
    print("5 - Sair.")
    opc = int(input("Digite uma opção:"))
    return opc

def main():
    opc = 0
    pilha = None

    while opc != 5:
        try:
            opc = menu()
            if opc == 1:
                try:
                    operacao = input("Digite uma operação matemática:")
                    pilha = inserir(pilha, operacao)
                except ValueError:
                    print("Erro ao digitar.")

            elif opc == 2:
                pilha = remover(pilha)

            elif opc == 3:
                mostrar_topo(pilha)

            elif opc == 4:
                mostrar_ope_pendentes(pilha)

            elif opc == 5:
                print("Até mais!")

            else:
                print("Tenta novamente!")

        except ValueError:
            print("Erro ao digitar.")

main()
