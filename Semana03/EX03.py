class No:
    def __init__(self, id, nome, artista, duracao):
        self.id = id
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        self.proximo = None
        self.anterior = None

class ListaDuplaEnca:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.musica_atual = None

    def inserir(self, id, nome, artista, duracao):
        novo = No(id, nome, artista, duracao)
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
            self.musica_atual = novo
        else:
            self.fim.proximo = novo
            novo.anterior = self.fim
            self.fim = novo
        print(f"Música {nome} adicionada a playlist com o ID {id}.")
        print(f"Artista: {artista} e duração da música: {duracao} minutos")

    def listar(self):
        if self.inicio is None:
            print("Playlist vazia.")
            return
        print("Playlist:")
        aux = self.inicio
        while aux is not None:
            print(f"Nome: {aux.nome}, ID: {aux.id}.")
            aux = aux.proximo

    def remover(self, nome):
        if self.inicio is None:
            print("Playlist vazia.")
            return

        aux = self.inicio
        while aux is not None and aux.nome != nome:
            aux = aux.proximo

        if aux is None:
            print(f"Música {nome} não encontrada.")
            return

        if aux == self.musica_atual:
            if aux.proximo:
                self.musica_atual = aux.proximo
            else:
                self.musica_atual = aux.anterior
        
        if aux == self.inicio and aux == self.fim:
            self.inicio = None
            self.fim = None
            self.musica_atual = None
        elif aux == self.inicio:
            self.inicio = aux.proximo
            self.inicio.anterior = None
        elif aux == self.fim:
            self.fim = aux.anterior
            self.fim.proximo = None
        else:
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

        print(f"Música {nome} removida!")

    def buscar_nome(self, nome):
        if self.inicio is None:
            print("Sem músicas na lista.")
            return
        
        aux = self.inicio
        encontrado = False
        while aux != None:
            if aux.nome.upper() == nome.upper():
                print(f"Encontramos sua música: {aux.nome}")
                encontrado = True
            aux = aux.proximo
        if not encontrado:
            print(f"Música {nome}, não encontrada.")

    def buscar_artista(self, artista):
        if self.inicio is None:
            print("Sem músicas na lista.")
            return
        
        aux = self.inicio
        encontrado = False
        while aux != None:
            if aux.artista.upper() == artista.upper():
                print(f"Encontramos o artista {aux.artista} da faixa na lista.")
                encontrado = True
            aux = aux.proximo

        if not encontrado: 
            print(f"Não encontramos o artista {artista} na lista.")

    def duracao_total(self):
        if self.inicio is None:
            print("Playlist vazia.")
            return
        soma_duracao = 0
        aux = self.inicio
        while aux != None:
            soma_duracao += aux.duracao
            aux = aux.proximo
        print(f"Duração total da playlist: {soma_duracao} minutos")

    def avancar(self):
        if self.musica_atual is None:
            print("Playlist vazia.")
            return

        if self.musica_atual.proximo != None:
            self.musica_atual = self.musica_atual.proximo
            print(f"Tocando agora: {self.musica_atual.nome}.")
        else:
            print("Está tocando a última música da playlist.")

    def voltar(self):
        if self.musica_atual == None:
            print("Playlist vazia.")
            return
        
        if self.musica_atual.anterior != None:
            self.musica_atual = self.musica_atual.anterior
            print(f"Voltando para a faixa: {self.musica_atual.nome}")
        else:
            print("Já está tocando a primeira música da playlist.")

def menu():
    print("MENU:")
    print("1 - Adicionar música na playlist.")
    print("2 - Listar todas as músicas.")
    print("3 - Remover música da playlist.")
    print("4 - Buscar música.")
    print("5 - Mostrar duração da playlist em minutos(m).")
    print("6 - Avançar música / Voltar para a anterior.")
    print("7 - Sair.")

    opc = int(input("\nDigite uma opção:"))
    return opc

def main():
    lista = ListaDuplaEnca()
    opc = 0
    while opc != 7:
        opc = menu()

        if opc == 1:
            try:
                id = int(input("Adicione o ID da música:"))
                nome = input("Digite o nome da música:").upper()
                artista = input("Digite o autor dela:").upper()
                duracao = float(input("Digite a duração dela:"))
                lista.inserir(id, nome, artista, duracao)
            except ValueError:
                print("Erro, tente novamente!")
        elif opc == 2:
            lista.listar()
        elif opc == 3:
            nome = input("Digite o nome da música para a remoção:").upper()
            lista.remover(nome)
        elif opc == 4:
            try:
                opcao = int(input("Escolha um parâmetro para a escolha, nome(1) ou artista(2):"))
                if opcao == 1:
                    nome = input("Digite um nome para a busca:")
                    lista.buscar_nome(nome)
                elif opcao == 2:
                    artista = input("Digite um artista para a busca:")
                    lista.buscar_artista(artista)
            except ValueError:
                print("Erro, tente novamente!")
        elif opc == 5:
            lista.duracao_total()
        elif opc == 6:
            if lista.musica_atual:
                print(f"Tocando: {lista.musica_atual.nome} de {lista.musica_atual.artista}")
            print("1 - Avançar música.")
            print("2 - Voltar música.")
            try:
                opcao = int(input("Escolha uma opção:"))
                if opcao == 1:
                    lista.avancar()
                elif opcao == 2:
                    lista.voltar()
            except ValueError:
                print("Erro, tente novamente!")
        elif opc == 7:
            print("Até mais bixo véio!\n")
        else:
            print("Digite outra opção, esta é inválida!")

main()
