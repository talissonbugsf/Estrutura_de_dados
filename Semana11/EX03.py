n = int(input("Digite um número:"))

def recursiva(n, soma_impares=0):
    if n == 0:
        print(f"Soma dos ímpares: {soma_impares}")
        return
    if n % 2 != 0:
        soma_impares += n
    recursiva(n - 1, soma_impares)

recursiva(n)
