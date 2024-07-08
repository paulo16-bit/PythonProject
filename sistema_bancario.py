menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("operação falhou! O valor informado é invalido")

    elif opcao == 's':
        valor = float(input("Informe o valor do saque: "))
        
        if valor>saldo:
            print("Operação falhou! Saldo insuficiente")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite")
        elif numero_saque >= LIMITE_SAQUE:
            print("Operação falhou! Número maximo de saque excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
        else:
            print("Operação falhou! O valor informado é invalido")
    
    elif opcao == 'e':
        print("\n============= EXTRATO =============")
        print("Não foram relizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================")
    
    elif opcao == 'q':
        break

    else:
        print("Operação invalida! Por favor selecione novamente a operação desejada")