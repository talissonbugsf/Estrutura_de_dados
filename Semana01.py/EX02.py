class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

agenda = []

talissa = Contato("Talissa", 99687235, "talissabugs@gmail.com")
marcia = Contato("Márcia", 97010194, "marciabugs.gmail.com")
girlei = Contato("Girlei", 99750156, "girleibugs.gmail.com")

agenda.extend([talissa, marcia, girlei])

for c in agenda:
    print(f"Nome:{c.nome}, Telefone:{c.telefone}, Email:{c.email}")
