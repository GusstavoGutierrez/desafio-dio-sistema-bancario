menu =  """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=>"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).strip().lower()

    if opcao == "d" or opcao == "depositar":
        try:
            valor = float(input("\nInforme o valor do depósito: ").replace(",", "."))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("\nOperação falhou! O valor informado é inválido.")
        except ValueError:
            print("\nOperação falhou! Valor inválido. Tente novamente.")

    elif opcao == "s" or opcao == "sacar":
        try:
            valor = float(input("\nInforme o valor do saque: ").replace(",", "."))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("\nOperação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("\nOperação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("\nOperação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("\nOperação falhou! O valor informado é inválido.")
        except ValueError:
            print("\nOperação falhou! Valor inválido. Tente novamente.")

    elif opcao == "e" or opcao == "extrato":
        print("\n================ EXTRATO ================\n")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================\n")

    elif opcao == "q" or opcao == "sair":
        print("\nObrigado por utilizar nosso sistema bancário!")
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")