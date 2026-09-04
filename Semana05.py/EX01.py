class No:
    def __init__(self, id, bastao=False):
        self.id = id
        self.bastao = bastao
        self.proximo = None
        self.anterior = None

def adicionar(lista, id, bastao=False):
    no = No(id, bastao)

    if lista is None:
            no.proximo = no
            no.anterior = no
            return no

    ultimo = lista.anterior
    no.proximo = lista
    no.anterior = ultimo
    ultimo.proximo = no
    lista.anterior = no

    return lista


def excluir(lista, id):
    if lista is None:
        print("Sem atletas!")
        return None
    aux = lista
    while True:
        if aux.id == id:
            if aux.proximo == aux:
                print(f"Único atleta na lista exluído {id}.")
                return None
            if aux.bastao:
                aux.proximo.bastao = True
                print(f"O atleta {id} estava com o bastão. O bastão foi passado para o atleta {aux.proximo.id}.")
            aux.proximo.anterior = aux.anterior
            aux.anterior.proximo = aux.proximo
            if aux == lista:
                lista = aux.proximo
            print(f"Atleta {id} removido!")
            return lista
        aux = aux.proximo
        if aux == lista: 
            break
    print("Atleta não encontrado!")
    return lista


def simular(lista, turnos):
    if lista is None:
        print("Não há atletas para realizar a simulação!")
        return

    aux = lista
    portador = None
    
    while True:
        if aux.bastao:
            portador = aux
            break
        aux = aux.proximo
        if aux == lista:
            break

    if portador is None:
        portador = lista
        portador.tem_bastao = True

    for turno in range(1, turnos + 1):
        print(f"Turno {turno}: Atleta {portador.id} está com o bastão.")
        
        portador.tem_bastao = False
        portador = portador.proximo
        portador.tem_bastao = True


def menu():
    print("1 - Adicionar atleta.")
    print("2 - Exluir atleta.")
    print("3 - Mostrar quem está segurando.")
    print("4 - Sair.")
    opc = int(input("Digite a opção:"))
    return opc

def main():
    lista = None
    opc = 0

    while opc != 4:
        opc = menu()

        if opc == 1:
            id = int(input("Digite o id do atleta:"))
            tem_bastao = True if lista is None else False
            lista = adicionar(lista, id, bastao=tem_bastao)
            print(f"Atleta {id} adicionado com sucesso!")

        elif opc == 2:
            id = int(input("Digite o id para remoção:"))
            lista = excluir(lista, id)

        elif opc == 3:
            turnos = int(input("Quantos turnos quer simular:"))
            simular(lista, turnos)

        elif opc == 4:
            print("Até mais!")

        else:
            print("Tenta denovo meu nobre!")

main()
