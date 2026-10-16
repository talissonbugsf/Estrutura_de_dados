def contagem_regressiva(n):
    if n == 11:
        return
    contagem_regressiva(n + 1)
    print("Contagem regressiva:", n)

contagem_regressiva(1)
