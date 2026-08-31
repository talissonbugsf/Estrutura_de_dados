import random

class Paciente:

    def __init__(self, código, nome, idade, prioridade_atendimento):
        self.codigo = código
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade_atendimento
        self.proximo = None
        self.anterior = None

class Lista_Dupla:

    def __init__(self):
        self.inicio = None
        self.fim = None

    def cadastro(self, codigo, nome, idade, prioridade):
        paciente_novo = Paciente(codigo, nome, idade, prioridade)
        if self.inicio is None:
            self.inicio = paciente_novo
            self.fim = paciente_novo
        else:
            self.fim.proximo = paciente_novo
            paciente_novo.anterior = self.fim
            self.fim = paciente_novo
        print(f"Paciente {nome} com a idade {idade} foi cadastrado com o seguinte código e prioridade de atendimento:")
        print(f"Código:{codigo}, Prioridade:{prioridade}.")

    def remover(self, codigo):
        if self.inicio is None:
            print("Sem pacientes.")
            return
        aux = self.inicio
        while aux != None:
            if aux.codigo == codigo:
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
                print(f"Paciente {aux.nome} removido!"
                      f"Código: {aux.codigo}"
                      )
            else:
                print(f"Paciente com o código '{codigo}' não encontrado!")
            aux = aux.proximo

    def localizar(self, codigo):
        if self.inicio is None:
            print("Sem pacientes.")
            return
        aux = self.inicio
        while aux is not None:
            if codigo == aux.codigo:
                print(f"Paciente localizado pelo código:{aux.codigo}.")
            else:
                print(f"Paciente com o código:{codigo} não encontrado.")
            aux = aux.proximo

    def atender_urgencia(self):
        if self.inicio is None:
            print("Sem pacientes.")
            return
        for emergencia in range(1, 6):
            aux = self.inicio
            while aux is not None:
                if aux.prioridade == emergencia:
                    print(f"Paciente {aux.nome} com o código {aux.codigo}."
                        f"Chamando para o atendimento; nível de emergência:{aux.prioridade}."
                          )
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
                    return
                aux = aux.proximo

            print("Nenhum paciente pendente.")

    def listar_crescente(self):
        if self.inicio is None:
            print("Sem pacientes.")
            return

        print("LISTA DE PACIENTES (Primeiro ao Último):")
        aux = self.inicio
        while aux is not None:
            print(
                f"Código: {aux.codigo}, Nome: {aux.nome}, Idade: {aux.idade};"
                f" Prioridade: {aux.prioridade}"
            )
            aux = aux.proximo

    def listar_prioridade(self, prio):
        if self.inicio is None:
            print("Sem pacientes.")
            return

        print(f"PACIENTES COM PRIORIDADE ({prio}):")
        encontrados = 0
        aux = self.inicio

        while aux is not None:
            if aux.prioridade == prio:
                print(
                f"Código: {aux.codigo}, Nome: {aux.nome}, Idade: {aux.idade};"
                f" Prioridade: {aux.prioridade}"
                )
                encontrados += 1
                aux = aux.proximo

        if encontrados == 0:
            print("Nenhum paciente encontrado com esta prioridade.")

    def listar_decrescente(self):
        if self.inicio is None:
            print("Sem pacientes.")
            return
        print("LISTA DE PACIENTES (Último ao Primeiro):")
        aux = self.fim
        while aux is not None:
            print(
                f"Código: {aux.codigo}, Nome: {aux.nome}, Idade: {aux.idade};"
                f" Prioridade: {aux.prioridade}"
            )
            aux = aux.anterior

    def informar_qntd_pacientes(self):
        if self.inicio is None:
            print("Sem pacientes.")
            return
        soma_pacientes = 0
        aux = self.inicio
        while aux is not None:
            soma_pacientes += 1
            aux = aux.proximo
        print(f"Quantidade de pacientes aguardando atendimento:{soma_pacientes}.")


def menu():
    print("MENU:")
    print("1 - Cadastrar um paciente;")
    print("2 - Remover um paciente após atendimento;")
    print("3 - Localizar paciente pelo código;")
    print("4 - Atender um paciente mais urgente;")
    print("5 - Listar paciente do primeiro ao último;")
    print("6 - Listar pacientes por ordem de atendimento;")
    print("7 - Listar pacientes do último ao primeiro;")
    print("8 - Informar pacientes que aguardam atendimento;")
    print("9 - Sair.")
    opc = int(input("Digite a opção que deseja selecionar:"))
    return opc

def main():
    lista = Lista_Dupla()
    opc = 0

    while opc != 9:
        try:
            opc = menu()

            if opc == 1:
                codigo = random.randint(10000, 99999)
                nome = input("Digite o seu nome:").upper()
                idade = int(input("Digite a sua idade:"))
                prioridade = int(input("Descreva o quão urgente é seu atendimento de 1 a 5:"))
                if prioridade < 1 or prioridade > 5:
                    print("Prioridade inválida.")
                else:
                    lista.cadastro(codigo, nome, idade, prioridade)

            elif opc == 2:    
                codigo = int(input("Digite o código do paciente a ser removido:"))
                lista.remover(codigo)

            elif opc == 3:
                codigo = int(input("Digite o código do paciente para localizá-lo:"))
                lista.localizar(codigo)

            elif opc == 4:
                lista.atender_urgencia()

            elif opc == 5:
                lista.listar_crescente()

            elif opc == 6:
                prioridade_ = int(input("Digite a prioridade:"))
                if prioridade_ < 1 or prioridade_ > 5:
                    lista.listar_prioridade(prioridade_)
                else:
                    print("Prioridade inválida.")

            elif opc == 7:
                lista.listar_decrescente()

            elif opc == 8:
                lista.informar_qntd_pacientes()

            elif opc == 9:
                print("\nAté mais!")

            else:
                print("Erro ao digitar, tente novamente!\n")
        except ValueError:
            print("Entrada inválida!")
main()
