class ListaEncadeada:
    def __init__(self, nome, responsavel):
        self.nome = nome
        self.responsavel = responsavel
        self.proximo = None

def inserir(lista, nome, responsavel):
    novo = ListaEncadeada(nome, responsavel)

    if lista is None:
        lista = novo
        return lista

    novo.proximo = lista
    lista = novo
    return lista

def percorrer(lista):
    aux = lista

    if lista is None:
        print("Lista vazia!")
        return

    while aux is not None:
        print(f"\n - {aux.nome}, {aux.responsavel};")
        aux = aux.proximo

def remover(lista, nome):
    if lista is None:
        print("Lista vazia!")
        return

    aux = lista
    anterior = None

    while aux is not None:
        if aux.nome == nome:
            if anterior is None:
                lista = aux.proximo
            else:
                anterior.proximo = aux.proximo

            return lista
        
        anterior = aux
        aux = aux.proximo

    print("Dado não encontrado")
    return lista

def main():
    lista = None
    lista = inserir(lista, "Planejamento do produto", "Ana")
    lista = inserir(lista, "Implementação do backend", "João")
    lista = inserir(lista, "Testes automatizados", "Carla")
    percorrer(lista)
    nome = "Planejamento do produto"
    lista = remover(lista, nome)
    percorrer(lista)

main()
