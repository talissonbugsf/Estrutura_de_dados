class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def calcular_bonus(self):
        if self.cargo == "Gerente":
            soma = self.salario * 0.10
            self.salario += soma
            print(f"Salário com bônus:{self.salario}")
        else:
            soma = self.salario * 0.05
            self.salario += soma
            print(f"Salário com bônus:{self.salario}")

gerson = Funcionario("Gerson", 7000, "Gerente")
eleomar = Funcionario("Eleomar", 2000, "Peão")

gerson.calcular_bonus()
eleomar.calcular_bonus()
           
