class No:
    def __init__(self, jogador):
        self.jogador = jogador
        self.proximo = None
        self.anterior = None


def inserir(fila_inicio, fila_fim, jogador_add):
    novo = No(jogador_add)

    if fila_inicio is None:
        return novo, novo

    fila_fim.proximo = novo
    novo.anterior = fila_fim
    fila_fim = novo
    return fila_inicio, fila_fim


def simular(fila_inicio, fila_fim):
    if fila_inicio is None:
        print("Fila vazia!")
        return fila_inicio, fila_fim

    if fila_inicio == fila_fim:
        print(f"{fila_inicio.jogador} jogou. Único jogador na fila, continua em 1º.")
        return fila_inicio, fila_fim

    jogador_atual = fila_inicio
    fila_inicio = fila_inicio.proximo
    fila_inicio.anterior = None

    jogador_atual.proximo = None
    jogador_atual.anterior = fila_fim
    fila_fim.proximo = jogador_atual
    fila_fim = jogador_atual

    print(f"{jogador_atual.jogador} jogou e foi para o final da fila.")
    return fila_inicio, fila_fim


def simular_rodadas(fila_inicio, fila_fim, rodadas):
    if fila_inicio is None:
        print("Fila vazia!")
        return fila_inicio, fila_fim

    print(f"\n--- Simulando {rodadas} rodadas ---")
    for i in range(rodadas):
        print(f"Rodada {i + 1}:")
        fila_inicio, fila_fim = simular(fila_inicio, fila_fim)
        mostrar_fila(fila_inicio)
        print("-" * 25)

    return fila_inicio, fila_fim


def mostrar_fila(fila_inicio):
    if fila_inicio is None:
        print("Fila vazia!")
        return

    contador = 1
    aux = fila_inicio
    print("\nFila atual:")
    while aux is not None:
        print(f"{contador}º - {aux.jogador}")
        contador += 1
        aux = aux.proximo


def mostrar_proximo(fila_inicio):
    if fila_inicio is None:
        print("Fila vazia!")
        return

    print(f"Próximo a jogar: {fila_inicio.jogador}")


def limpar_fila(fila_inicio):
    if fila_inicio is None:
        print("A fila já está vazia!")
        return None, None

    aux = fila_inicio
    while aux is not None:
        proximo_no = aux.proximo
        print(f"{aux.jogador} removido com sucesso!")
        aux = proximo_no

    print("A fila foi esvaziada!")
    return None, None


def menu():
    print("\n=== MENU SESSÃO DE JOGOS ===")
    print("1 - Adicionar jogador ao final da fila")
    print("2 - Simular 1 rodada")
    print("3 - Simular N rodadas")
    print("4 - Mostrar fila")
    print("5 - Mostrar próximo a jogar")
    print("6 - Limpar fila")
    print("7 - Sair")
    return int(input("Digite uma opção: "))


def main():
    opc = 0
    fila_inicio = None
    fila_fim = None

    while opc != 7:
        try:
            opc = menu()
            if opc == 1:
                jogador = input("Digite o nome do jogador: ").strip()
                if jogador:
                    fila_inicio, fila_fim = inserir(fila_inicio, fila_fim, jogador)
                    print(f"Jogador '{jogador}' adicionado à fila!")
                else:
                    print("Nome de jogador inválido.")
            elif opc == 2:
                fila_inicio, fila_fim = simular(fila_inicio, fila_fim)
            elif opc == 3:
                rodadas = int(input("Digite a quantidade de rodadas: "))
                if rodadas > 0:
                    fila_inicio, fila_fim = simular_rodadas(fila_inicio, fila_fim, rodadas)
                else:
                    print("Digite um número maior que zero.")
            elif opc == 4:
                mostrar_fila(fila_inicio)
            elif opc == 5:
                mostrar_proximo(fila_inicio)
            elif opc == 6:
                fila_inicio, fila_fim = limpar_fila(fila_inicio)
            elif opc == 7:
                print("Encerrando a sala de partidas. Até mais!")
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite um número correto.")


main()
