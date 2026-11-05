def recursiva(n):
    if n == -1:
        return
    print(f"Contagem regressiva: {n}")
    recursiva(n - 1)

def contagem_regressiva():
    while True:
        print("\nOpções: 1. Iniciar viagem; 2. Abortar missão;")
        try:
            opc = int(input("Digite uma opção para prosseguir: "))
            
            if opc == 1:
                n = int(input("Digite um número: "))
                recursiva(n)
            elif opc == 2:
                print("Suma da minha frente!")
                break
            else:
                print("Tenta de novo!")
                
        except ValueError:
            print("Erro! Digite um número válido.")

def main():
    contagem_regressiva()

main()
