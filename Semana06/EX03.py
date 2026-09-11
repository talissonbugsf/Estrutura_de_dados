import random

class No:
    def __init__(self,carros):
        self.carros = carros
        self.proximo = None

def carros_():
    pilha = None
    carros_1 = ["Gol", "Fiesta", "Corolla", "Palio", "Ecosport", 
                "S10", "Hilux", "Uno", "Jetta", "Civic", "Fusca", "Marea",
                "Peugeot 206", "RAV4", "Camaro", "HB20", "Duster", "Chevette",
                "Del rey", "Tracker"]
    
    carros_sorteados = random.sample(carros_1, 20)
    
    for i in range(20):
        carro_sorteado = carros_sorteados[i]
        novo = No(carro_sorteado)
        novo.proximo = pilha
        pilha = novo
    return pilha

def mostrar(pilha):
    if pilha is None:
        print("Garagem vazia!")
        return
    print("\nCARROS:")
    aux = pilha
    contador = 1
    while aux is not None:
        print(f"{contador} - {aux.carros}")
        contador += 1
        aux = aux.proximo

def verificar(pilha, carro__):
    if pilha is None:
        return False
    aux = pilha
    while aux is not None:
        if aux.carros.strip().upper() == carro__.strip().upper():
            return True
        aux = aux.proximo
    return False

def remover(pilha, carro___):
    if pilha is None:
        print("Garagem vazia!")
        return None

    if not verificar(pilha, carro___):
        print(f"O carro ({carro___}) não está na garagem")
        return pilha

    print("Começando remoção...")
    removidos = []

    while pilha is not None:
        carro_removido = pilha.carros
        removidos.append(carro_removido)
        pilha = pilha.proximo  # Desempilha o topo atual
        
        # Só para de desempilhar quando chegar no carro solicitado
        if carro_removido.strip().upper() == carro___.strip().upper():
            break
            
    print(f"Carros retirados: {', '.join(removidos)}")
    print("Remoção feita!")
    return pilha

def main():
    opc = 0
    pilha = carros_()
    while opc != 2:
        mostrar(pilha)
        print("\nOPÇÕES:")
        print("1 - Remover um carro.")
        print("2 - Sair.")
        try:
            opc = int(input("Digite uma opção:"))
            if opc == 1:
                if pilha is None:
                    print("Sem carros na garagem!")
                    continue
                carro = input("\nDigite o carro que você deseja retirar:").strip()
                pilha = remover(pilha, carro)

            elif opc == 2:
                print("Até mais!")

            else:
                print("Erro ao digitar.")

        except ValueError:
            print("Erro ao digitar.")

main()
