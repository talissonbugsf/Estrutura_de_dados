class ContaBancaria:

    def __init__(self, nome_do_titular, numero_da_conta, saldo):
        self.titular = nome_do_titular
        self.numero_conta = numero_da_conta
        self.saldo = saldo

    def consultar_saldo(self):
        print(f"Saldo de {self.titular}: R$ {self.saldo}")

    def realizar_deposito(self):
        valor = float(input("Deseja realizar um depósito de quanto: R$ "))
        if valor > 0:
            self.saldo += valor
            print(f"Depósito realizado com sucesso! Novo saldo: R$ {self.saldo}")
        else:
            print("Operação cancelada: O valor do depósito deve ser maior que zero!")

    def realizar_saque(self):
        valor = float(input("Deseja retirar qual valor da conta: R$ "))
        if valor <= 0:
            print("Operação cancelada: O valor do saque deve ser maior que zero!")
        elif valor > self.saldo:
            print("Operação cancelada: Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso!")
            print(f"Saldo restante: R$ {self.saldo}")

    def transferir(self, conta_destino):
        valor = float(input(f"Digite o valor que deseja transferir para {conta_destino.titular}: R$ "))
        if valor <= 0:
            print("Operação cancelada: O valor da transferência deve ser maior que zero!")
        elif valor > self.saldo:
            print("Operação cancelada: Saldo insuficiente.")
        else:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f"Transferência de R$ {valor} realizada para {conta_destino.titular} com sucesso!")
            print(f"Seu saldo restante: R$ {self.saldo}")


def menu():
    print("MENU:")
    print("1 - Consultar saldo")
    print("2 - Realizar um depósito")
    print("3 - Realizar um saque")
    print("4 - Transferir para outra conta")
    print("5 - Trocar de conta / Sair")
    return int(input("Digite uma opção: "))


def contas():
    print("CONTAS BANCÁRIAS")
    print("1 - Geraldino (Conta 423560)")
    print("2 - Junaia (Conta 560219)")
    print("3 - Sair.")
    return int(input("Escolha uma opção: "))


def main():
    qntd_ini1 = float(input("Digite o saldo inicial da Conta 1 (Geraldino): R$ "))
    qntd_ini2 = float(input("Digite o saldo inicial da Conta 2 (Junaia): R$ "))

    conta1 = ContaBancaria("Geraldino", 423560, qntd_ini1)
    conta2 = ContaBancaria("Junaia", 560219, qntd_ini2)

    while True:
        acesso = contas()

        if acesso == 1:
            conta_atual = conta1
            outra_conta = conta2
        elif acesso == 2:
            conta_atual = conta2
            outra_conta = conta1
        elif acesso == 3:
            print("Até mais!")
            break
        else:
            print("Opção inválida!")
            continue

        opc = 0
        while opc != 5:
            print(f"Usuário:{conta_atual.titular}")
            opc = menu()

            if opc == 1:
                conta_atual.consultar_saldo()
            elif opc == 2:
                conta_atual.realizar_deposito()
            elif opc == 3:
                conta_atual.realizar_saque()
            elif opc == 4:
                conta_atual.transferir(outra_conta)
            elif opc == 5:
                print(f"Saindo da conta de {conta_atual.titular}")
            else:
                print("Opção inválida, tente novamente.")

main()
