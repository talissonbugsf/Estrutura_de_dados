import random

class No:
    def __init__(self, guerreiros):
        self.guerreiros = guerreiros
        self.proximo = None
        self.anterior = None

def add_guerreiros(qntd_guerreiros):
    if qntd_guerreiros <= 0:
        return None
    cabeca = No(1)
    aux = cabeca
    for i in range(2, qntd_guerreiros + 1):
        novo_no = No(i)
        aux.proximo = novo_no
        novo_no.anterior = aux
        aux = novo_no
    aux.proximo = cabeca
    cabeca.anterior = aux

    return cabeca


def simular(qntd_guerreiros):
    if qntd_guerreiros <= 0:
        print("Sem guerreiros")
        return

    cabeca = add_guerreiros(qntd_guerreiros)
    aux = cabeca
    total_restante = qntd_guerreiros
    rodada = 1
    print("\nInicio do game")
    while total_restante > 1:
        passos = random.randint(1, total_restante)
        for _ in range(passos - 1):
            aux = aux.proximo
        eliminado = aux
        print(f"Rodada {rodada}: Guerreiro {eliminado.guerreiros} foi eliminado!")
        eliminado.anterior.proximo = eliminado.proximo
        eliminado.proximo.anterior = eliminado.anterior
        aux = eliminado.proximo
        eliminado.proximo = None
        eliminado.anterior = None
        total_restante -= 1
        rodada += 1
    print(f"\nO SOBREVIVENTE FOI O GUERREIRO {aux.guerreiros}!")

def menu():
    print("OPÇÕES:")
    print("1 - Simular partida.")
    print("2 - Sair do jogo.")
    try:
        opc = int(input("Digite uma opção:"))
        return opc
    except ValueError:
        return 0

def main():
    lista = None
    opc = 0
    try:
        while opc != 2:
            opc = menu()

            if opc == 1:
                try:
                    guerreiros = int(input("Quantidade de guerreiros:"))
                    simular(guerreiros)
                except ValueError:
                    print("Erro, tenta denovo!")

            elif opc == 2:
                print("Até mais!!!")

            else:
                print("Tenta denovo!!")

    except ValueError:
        print("Aí não cara, tenta denovo!")

main()
