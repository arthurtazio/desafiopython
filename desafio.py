menu = """

[Dep] Depositar
[Sac] Sacar
[Ext] Extrato
[Sair] Sair

=>  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)


    if opcao == "Dep":
        valor = float(input("informeo valor do depósito:    "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito:  R$ {valor:.2f}\n"

        else:
            print("Operação falhou! Informe um valor válido")
     
    elif opcao == "Sac":
        valor = float(input("informe o valor do saque:  "))

        excedeu_saldo = valor > saldo

        exedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_saques:
            print("Operação falhou! Número de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saques: R$ {valor: .2f}\n"
            numero_saques += 1

        else:
            print("Operaçao falhou! Valor inválido")

    elif opcao == "Ext":
        print("\n================ EXTRATO ===============")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================================")

    elif opcao == "Sair":
        break

    else:
        print("Operaçao inválida, Por favor selecione uma operação válida.")
