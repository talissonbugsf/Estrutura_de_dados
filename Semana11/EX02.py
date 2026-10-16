n = int(input("Digite um número:"))

def recursiva(n):
    if n == 0:
        return
    if n % 2 == 0:
        print(f"Números pares: {n}")
    recursiva(n - 1)

recursiva(n)
