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
            return "Reprovado!"
        else:
            return "Aprovado!"

notas1 = [8, 9, 3]
notas2 = [10, 5, 6]
notas3 = [10, 9.9, 10]

aluno1 = Aluno("Bobbie", notas1)
aluno1.calcular_media()

aluno2 = Aluno("Maria", notas2)
aluno2.calcular_media()

aluno3 = Aluno("Vinicíus", notas3)
aluno3.calcular_media() 

turma = [aluno1, aluno2, aluno3]

for aluno in turma:
    print(f"Aluno: {aluno.nome}; Média: {aluno.media}; Situação: {aluno.verificar_aprovacao()}.")
