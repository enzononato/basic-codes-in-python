import os
import time

os.system('cls')


saldo = 0
limite = 500
extrato = ""
numero_saques = 0


menu = """
========== MENU ===========

[d] Depositar
[s] Sacar
[e] Extrato
[s] Sair

"""




while True:

    opcao = input(menu)

    if opcao == '1':
        os.system('cls')
        valorDeposito = float(input("Informe o valor do depósito: "))
        if valorDeposito > 0:
            saldo+=valorDeposito
            extrato += '\nDEPÓSITO -> R$'+str(valorDeposito)
            print("Depósito efetuado com Sucesso!!!")
        else:
            print("Valor de depósito inválido!")

    elif opcao == '2':
        os.system('cls')
        valorSaque = float(input("Informe o valor do saque: "))
        if valorSaque > limite:
            print("\nO valor do seu saque não pode exceder R$ 500,00\n")
        if valorSaque > saldo:
            print("Você não pode sacar um valor maior que o seu saldo")
        if valorSaque <= limite and valorSaque > 0 and numero_saques < 3 and valorSaque < saldo:
            saldo-=valorSaque
            extrato += '\nSAQUE -> R$'+str(valorSaque)
            numero_saques += 1
        elif numero_saques >= 3:
            print("Você já fez os seus 3 saques diários")
        else:
            print("Valor Inválido!")
        

    elif opcao == '3':
        os.system('cls')
        print(extrato)
        print(f'\nSALDO = {saldo}')

    elif opcao == '0':
        break

    else:
        os.system('cls')
        print('Opção inválida tente novamente...')    
        time.sleep(2)