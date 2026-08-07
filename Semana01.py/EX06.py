class Aluno:

    def __init__(self, nome, lista):
        self.nome = nome
        self.lista = lista
        self.media = 0

    def calcular_media(self):
        soma = 0
        for i in range(len(self.lista)):
            soma += self.lista[i]
        self.media = soma / len(self.lista)
        return self.media

    def verificar_aprovacao(self):
        if self.media < 7:
            print(f"Aluno:{self.nome}, Situação:Reprovado!")
        else:
             print(f"Aluno:{self.nome}, Situação:Aprovado!")


notas1 = [8, 9, 3]
notas2 = [10,5,6]

aluno1 = Aluno("Bobbie", notas1)
aluno1.calcular_media()
aluno1.verificar_aprovacao()

aluno2 = Aluno("Maria", notas2)
aluno2.calcular_media()
aluno2.verificar_aprovacao()
