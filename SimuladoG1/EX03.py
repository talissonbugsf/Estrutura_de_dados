class Circular:
    def __init__(self, nome, duracao, ambiente, ativo):
        self.nome = nome
        self.duracao = duracao
        self.ambiente = ambiente
        self.ativo = ativo

def adicionar(lista, nome, duracao, ambiente, ativo):
    novo = Circular(nome, duracao, ambiente, ativo)
    
    if lista is None:
        novo.proximo = novo
        novo.anterior = novo
        return lista

    novo.proximo = lista
    novo.anterior = lista.anterior
    lista.anterior.proximo = novo
    lista.anterior = novo
    return lista

def listar(lista):
    if lista is None:
        print("Lista vazia!")   
        return
    aux = lista
    while True:
        if aux.ambiente == "teste":
            print(f"{aux.nome}, {aux.ambiente};")
        aux = aux.proximo
        if aux == lista:
            break
    while True:
        if aux.ambiente == "homologação":
            print(f"{aux.nome}, {aux.ambiente};")
        aux = aux.proximo
        if aux == lista:
            break
    while True:
        if aux.ambiente == "produção":
            print(f"{aux.nome}, {aux.ambiente};")
        aux = aux.proximo
        if aux == lista:
            break

def listar_ativos(lista):
    if lista is None:
        print("Lista vazia!")
        return

    aux = lista
    while aux is not None:
        print(f" - {aux.nome}, {aux.ativo}")
        aux = aux.proximo

def exibir(lista):
    if lista is None:
        print("Lista vazia")
        return
    aux = lista
    total_tempo = 0
    while True:
        total_tempo += aux.duracao
        aux = aux.proximo
        if aux == lista:
            break
    print(f"Tempo total: {total_tempo}")

def ativar(lista, nome):
    if lista is None:
        print("Lista vazia!")
        return
    aux = lista
    while aux is not None:
        if aux.nome == nome:
            if aux.ativo == False:
                aux.ativo = True
                return lista
        aux = aux.proximo
        if aux == lista:
            break
    print(f"{nome} não encontrado!")

def desativar(lista, nome):
    if lista is None:
        print("Lista vazia!")
        return
    aux = lista
    while aux is not None:
        if aux.nome == nome:
            if aux.ativo == True:
                aux.ativo = False
                return lista
        aux = aux.proximo
        if aux == lista:
            break
    print(f"{nome} não encontrado!")

def remover(lista, nome):
    if lista is None:
        print("Lista vazia!")
        return
    aux = lista
    while True:
        if aux.nome == nome:
            if aux.proximo == aux:
                return None
            elif aux == lista:
                lista.proximo.anterior = lista.anterior
                lista.anterior.proximo = lista.proximo
                lista = lista.proximo
                return lista
            else:
                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior
                return lista
        elif aux.proximo == lista:
            print(f"{aux.nome} não encontado")
            return lista 
        aux = aux.proximo

def menu():
    print("MENU:")
    print("1 - Inserir.")
    print("2 - Listar.")
    print("3 - Exibir.")
    print("4 - Ativar.")
    print("5 - Desativar.")
    print("6 - Remover.")
    print("7 - Sair.")
    opc = int(input("Digite uma opção:"))
    return opc

def main():
    opc = 0
    lista = None
    while opc != 7:
        try:
            opc = menu()
            if opc == 1:
                nome = input("Digite seu nome:").title()
                duracao = int(input("Digite a duração em segundos:"))
                ambiente = input("Digite o ambiente:")
                ativo = True
                lista = adicionar(lista, nome, duracao, ambiente, ativo)
            elif opc == 2:
                opcao = 0
                while opcao > 2 or opcao < 1:
                    opcao = int(input("Digite a opção:"))
                if opcao == 1:
                    listar(lista)
                elif opcao == 2:
                    listar_ativos(lista)
            elif opc == 3:
                exibir(lista)
            elif opc == 4:
                nome = input("Digite o nome para a troca:")
                lista = ativar(lista, nome)
            elif opc == 5:
                nome = input("Digite o nome para a troca:")
                lista = desativar(lista, nome)
            elif opc == 6:
                nome = input("Digite o nome para remoção:")
                lista = remover(lista, nome)
            elif opc == 7:
                print("Até mais!")
            else:
                print("Tenta denovo!")
        except ValueError:
            print("Tenta denovo!")

main()    
