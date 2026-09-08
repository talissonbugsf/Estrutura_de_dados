import random
class No:
    def __init__(self, cliente):
        self.cliente = cliente
        self.proximo = None
        self.anterior = None

def mesa(cliente):
    if cliente <= 0:
        return None
    cabeca = No(1)
    aux = cabeca

    for i in range(2, cliente + 1):
        novo_no = No(i)
        aux.proximo = novo_no
        novo_no.anterior = aux
        aux = novo_no
    aux.proximo = cabeca
    cabeca.anterior = aux

    return cabeca

def adicionar_cliente(cabeca, id_cliente):
    novo_no = No(id_cliente)
    if cabeca is None:
        novo_no.proximo = novo_no
        novo_no.anterior = novo_no
        return novo_no
    
    ultimo = cabeca.anterior
    ultimo.proximo = novo_no
    novo_no.anterior = ultimo
    novo_no.proximo = cabeca
    cabeca.anterior = novo_no
    return cabeca

def remover_cliente(cabeca, no_remover):
    if cabeca is None or no_remover is None:
        return None, None
    if cabeca.proximo == cabeca and cabeca == no_remover:
        return None, None
    
    proximo_no = no_remover.proximo
    no_remover.anterior.proximo = no_remover.proximo
    no_remover.proximo.anterior = no_remover.anterior
    
    nova_cabeca = proximo_no if cabeca == no_remover else cabeca
    return nova_cabeca, proximo_no

def simular(cliente):
    if cliente <= 0:
        print("Sem clientes!")
        return

    cabeca = mesa(cliente)
    aux = cabeca
    total_restante = cliente
    proximo_id = cliente + 1

    print("\nComeçando o rodízio.")

    while total_restante > 1:
        passos = random.randint(1, 5)
        
        print(f"A fatia de pizza está passando...")
        for _ in range(passos):
            aux = aux.proximo
            print(f"Cliente {aux.cliente} recebeu a fatia.")
        acao = random.choice(["nada", "adicionar", "remover"])
        if acao == "adicionar":
            cabeca = adicionar_cliente(cabeca, proximo_id)
            total_restante += 1
            print(f"Cliente {proximo_id} entrou na mesa!")
            proximo_id += 1
        elif acao == "remover" and total_restante > 1:
            cliente_removido = aux.cliente
            cabeca, aux = remover_cliente(cabeca, aux)
            total_restante -= 1
            print(f"Cliente {cliente_removido} se mandou!")
    print(f"\nRodízio encerrado! Apenas{aux.cliente} sobrou.")

def menu():
    print("\nOPÇÕES:")
    print("1 - Simular rodízio.")
    print("2 - Sair.")
    try:
        opc = int(input("Escolha uma opção: "))
        return opc
    except ValueError:
        print("Erro ao digitar.")
        return -1

def main():
    opc = 0
    while opc != 2:
        opc = menu()
        if opc == 1:
            try:
                cliente = int(input("Digite a quantidade de clientes: "))
                simular(cliente)
            except ValueError:
                print("Erro, tenta denovo!")
        elif opc == 2:
            print("Até mais!!")
        else:
            print("Erro, tenta denovo!")

main()
