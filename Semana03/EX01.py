class NoAluno:
    def __init__(self, ID, Nome, Nota):
        self.id = ID
        self.nome = Nome
        self.nota = Nota
        self.proximo = None
        self.anterior = None


class ListaDuplaEnca:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir(self, ID, Nome, Nota):
        novo = NoAluno(ID, Nome, Nota)
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            novo.anterior = self.fim
            self.fim = novo
        print(f"Aluno {Nome} inserido com sucesso!")

    def listar(self):
        if self.inicio is None:
            print("A lista de alunos está vazia.")
            return

        print("LISTA DE ALUNOs:")
        aux = self.inicio
        while aux is not None:
            print(f"ID:{aux.id}, Nome:{aux.nome}, Nota: {aux.nota}")
            aux = aux.proximo

    def remover(self, ID):
        if self.inicio is None:
            print("A lista está vazia.")
            return

        aux = self.inicio
        while aux is not None and aux.id != ID:
            aux = aux.proximo

        if aux is None:
            print(f"Aluno com ID {ID} não foi encontrado.")
            return

        if aux == self.inicio and aux == self.fim:
            self.inicio = None
            self.fim = None
        elif aux == self.inicio:
            self.inicio = aux.proximo
            self.inicio.anterior = None
        elif aux == self.fim:
            self.fim = aux.anterior
            self.fim.proximo = None
        else:
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

        print(f"Aluno ID {ID} removido com sucesso!")

    def mostrar_situacao(self, ID):
        if self.inicio is None:
            print("A lista está vazia.")
            return

        aux = self.inicio
        while aux is not None:
            if aux.id == ID:
                print(f"Aluno cadastrado! ID: {aux.id}, Nome: {aux.nome}, Nota: {aux.nota}")
                return
            aux = aux.proximo

        print(f"Aluno inexistente.")

    def listar_por_classificacao(self):
        if self.inicio is None:
            print("A lista de alunos está vazia.")
            return

        print("CLASSIFICAÇÃO DOS ALUNOS:")
        aux = self.inicio
        while aux is not None:
            if aux.nota >= 7.0:
                status = "Aprovado"
            elif 4.0 <= aux.nota < 7.0:
                status = "Exame"
            else:
                status = "Reprovado"

            print(f"{status} ID: {aux.id}, Nome: {aux.nome}, Nota: {aux.nota}")
            aux = aux.proximo


def menu():
    print("\nMENU PRINCIPAL:")
    print("1 - Inserir aluno")
    print("2 - Listar alunos")
    print("3 - Remover aluno")
    print("4 - Mostrar situação do aluno")
    print("5 - Listar alunos por classificação")
    print("6 - Sair")

    return int(input("\nInsira a opção desejada: "))


def main():
    lista = ListaDuplaEnca()

    opc = 0
    while opc != 6:
        opc = menu()

        if opc == 1:
            id_aluno = int(input("Digite o ID do aluno: "))
            nome = input("Digite o Nome do aluno: ")
            nota = float(input("Digite a Nota final do aluno: "))
            lista.inserir(id_aluno, nome, nota)
        elif opc == 2:
            lista.listar()
        elif opc == 3:
            id_aluno = int(input("Digite o ID do aluno a ser removido: "))
            lista.remover(id_aluno)
        elif opc == 4:
            id_aluno = int(input("Digite o ID do aluno para buscar: "))
            lista.mostrar_situacao(id_aluno)
        elif opc == 5:
            lista.listar_por_classificacao()
        elif opc == 6:
            print("\nEncerrando o sistema...")
        else:
            print("\nOpção inválida!")


main()
