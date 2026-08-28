class Aluno:

    def __init__(self, matricula, nome, situacao, nota_final):
        self.Matricula = matricula
        self.Nome = nome
        self.Situacao = situacao
        self.Nota = nota_final
        self.Proximo = None

class Turma:

    def __init__(self):
        self.inicio = None

    def cadastrar(self, matricula, nome,  nota_final):
        novo = Aluno(matricula, nome, True, nota_final)
        if self.inicio is None:
            self.inicio = novo
        else:
            aux = self.inicio
            while aux.Proximo is not None:
                aux = aux.Proximo
            aux.Proximo = novo

        print(f"Aluno {nome} com o código de matrícula ({matricula}) adicionado ao sistema!")
        print(f"Situação: Ativo, Nota: {nota_final}.")

    def listar(self):
        if self.inicio is None:
            print("Sem alunos cadastrados!")
            return
        print("\nLISTA DE ALUNOS:")
        aux = self.inicio
        while aux is not None:
            print(f"Aluno: {aux.Nome}; Matrícula: {aux.Matricula}")
            aux = aux.Proximo

    def listar_situacao(self, situacao):
        if self.inicio is None:
            print("Sem alunos cadastrados!")
            return

        status = "ATIVOS" if situacao else "DESATIVADOS"
        print(f"ALUNOS {status}")
        encontrou = False
        aux = self.inicio
        while aux is not None:
            if aux.Situacao == situacao:
                print(f"Aluno {aux.Nome} encontrado.")
                encontrou = True
            aux = aux.Proximo
        if not encontrou:
            print("Não encontrado!")


    def buscar(self, busca):
        if self.inicio is None:
            print("Sem alunos cadastrados.")
            return
        aux = self.inicio
        while aux is not None:
            if aux.Matricula == busca:
                print(f"Aluno encontrado com o código de matrícula: {aux.Matricula}.")
            aux = aux.Proximo

    def alterar_nota(self, matricula, nova_nota):
        if self.inicio is None:
            print("Sem alunos cadastrados.")
            return
        aux = self.inicio
        while aux is not None:
            if matricula == aux.Matricula:
                aux.Nota = nova_nota
                print(f"Aluno {aux.Nome} teve sua nota alterada {aux.Nota}.")
            aux = aux.Proximo

    def alterar_situacao(self, matricula):
        if self.inicio is None:
            print("Sem alunos cadastrados.")
            return
        aux = self.inicio
        while aux is not None:
            if aux.Matricula == matricula:
                aux.Situacao = not aux.Situacao
                status = "Ativo" if aux.Situacao else "Inativo"
                print(f"Nova situação({status}) para o aluno: {aux.Nome}.")
                return
            aux = aux.proximo
        
    def remover(self, matricula):
        if self.inicio is None:
            print("Sem alunos cadastrados.")
            return
        
        if self.inicio.Matricula == matricula:
            print(f"Aluno {self.inicio.Nome} removido do sistema!")
            self.inicio = self.inicio.Proximo
            return

        anterior = self.inicio
        aux = self.inicio.Proximo

        while aux is not None:
            if aux.Matricula == matricula:
                anterior.Proximo = aux.Proximo
                print(f"Aluno {aux.Nome} removido do sistema!")
                return
            anterior = aux
            aux = aux.Proximo
        print("Aluno não encontrado para ser removido!")

    def qntd_alunos(self):
        if self.inicio is None:
            print("Sem alunos cadastrados.")
            return
        aux = self.inicio
        soma_alunos = 0
        while aux is not None:
            soma_alunos += 1
            aux = aux.Proximo
        print(f"Quantidade de alunos cadastrados: {soma_alunos}.")

    def media(self):
        if self.inicio is None:
            print("Sem alunos cadastrados.")
            return
        aux = self.inicio
        soma_notas = 0
        qntd = 0
        while aux is not None:
            soma_notas += aux.Nota
            qntd += 1
            aux = aux.Proximo
        media = soma_notas / qntd
        print(f"Média das notas dos alunos: {media}")

    def media_ativos(self):
        if self.inicio is None:
            print("Sem alunos cadastrados.")
            return
        aux = self.inicio
        soma_notas = 0
        qntd = 0
        while aux is not None:
            if aux.Situacao == True:
                soma_notas += aux.Nota
                qntd += 1
            aux = aux.Proximo
        media = soma_notas / qntd
        print(f"Média das notas dos alunos ativos: {media}")        

def menu():
    print("MENU:")
    print("1 - cadastrar um aluno no final da lista;")
    print("2 - listar todos os alunos cadastrados;")
    print("3 - listar apenas alunos ativos no sistema;")
    print("4 - listar apenas alunos desativados no sistema;")
    print("5 - buscar um aluno pela matrícula;")
    print("6 - alterar nota final de um aluno;")
    print("7 - alterar a situação do aluno")
    print("8 - remover um aluno da lista;")
    print("9 - informar a quantidade de alunos cadastrados;")
    print("10 - calcular a média das notas da turma;")
    print("11 - calcular a média das notas dos alunos ativos no sistema;")
    print("12 - sair.")
    opc = int(input("\nDigite uma opção:"))
    return opc

def main():
    opc = 0
    turma = Turma()
    while opc != 12:
        opc = menu()

        if opc == 1:
            try:
                matricula = int(input("Digite um código de matrícula para o aluno:"))
                if turma.buscar(matricula):
                    print("Já existe um aluno com essa matrícula.")
                    continue
                nome = input("Digite o nome do aluno:").title()
                nota = float(input("Digite a nota do aluno:"))
                turma.cadastrar(matricula, nome, nota)
            except:
                print("Erro ao digitar.")
        elif opc == 2:
            turma.listar()

        elif opc == 3:
            turma.listar_situacao(True)

        elif opc == 4:
            turma.listar_situacao(False)

        elif opc == 5:
            try:
                busca = int(input("Digite o código de matrícula para a busca:"))
                turma.buscar(busca)
            except ValueError:
                print("Erro ao digitar.")

        elif opc == 6:
            try:
                matricula = int(input("Digite o código de matrícula a ser alterado:"))
                nova_nota = float(input("Digite uma nova nota:"))
                turma.alterar_nota(matricula, nova_nota)
            except ValueError:
                print("Erro ao digitar.")

        elif opc == 7:
            try:
                matricula = int(input("Digite o código de matrícula do aluno para alterar a situação:"))
                turma.alterar_situacao(matricula)
            except ValueError:
                print("Erro ao digitar.")

        elif opc == 8:
            try:
                codigo = int(input("Digite o código do aluno a ser removido:"))
                turma.remover(codigo)
            except ValueError:
                print("Erro ao digitar.")

        elif opc == 9:
            turma.qntd_alunos()

        elif opc == 10:
            turma.media()

        elif opc == 11:
            turma.media_ativos()

        elif opc == 12:
            print("\nAté mais!")

        else:
            print("Erro! Tente novamente.\n")


main()
