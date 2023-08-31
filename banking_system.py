
import os
import time

os.system('cls')


saldo = 0
limite = 500
extrato = ""
limiteSaques = 3
numeroSaques = 0
clientes= {}



def menu():
    return """
    ========== MENU ===========

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar Novo Usuário
    [0] Sair

    ===========================

    """

def funcao_deposito(saldo, valorDeposito, extrato,/):
    if valorDeposito > 0:
        saldo+=valorDeposito
        extrato += '\nDEPÓSITO -> R$'+str(valorDeposito)
        print("Depósito efetuado com Sucesso!!!")
    else:
        print("Valor de depósito inválido!")
    time.sleep(1)

    return saldo, extrato

def funcao_saque(*,saldo, valorSaque, extrato, limite, limiteSaques, numeroSaques):
    if valorSaque > saldo:
        print("Você não pode sacar um valor maior que o seu saldo")

    elif valorSaque > limite:
        print("\nO valor do seu saque não pode exceder R$ 500,00\n")

    elif valorSaque <= limite and valorSaque > 0 and numeroSaques < limiteSaques and valorSaque <= saldo:
        saldo-=valorSaque
        extrato += '\nSAQUE -> R$'+str(valorSaque)
        numeroSaques += 1

    elif numeroSaques >= limiteSaques:
            print(f"Você já fez os seus {limiteSaques} saques diários")
    else:
        print("Valor Inválido!")
    time.sleep(1)

    return saldo, extrato, numeroSaques



def mostrar_extrato(saldo,/,*,extrato):
    print(extrato)
    print(f'\nSALDO = {saldo}')


def cadastrar_usuário():
    nome = input("Informe seu nome: ")
    os.system("cls")

    data_nascimento = input("Informe sua data de nascimento: ")
    os.system("cls")

    cpf = input("Informe seu CPF: ")
    os.system("cls")

    if cpf in clientes.keys():
        print("CPF já existente")
    else:
        logradouro = input("Informe seu logradouro: ")
        os.system("cls")

        numero = input("Informe o número da casa: ")
        os.system("cls")

        bairro = input("Informe seu bairro: ")
        os.system("cls")

        cidade = input("Informe sua cidade: ")
        os.system("cls")

        estado = input("Informe a sigla do estado: ")
        os.system("cls")


        clientes.update({cpf : {"nome":nome, "data de nascimento":data_nascimento, "logradouro":logradouro, "numero":numero, "bairro":bairro, "cidade":cidade, "estado":estado}})

    time.sleep(1)


while True:

    opcao = input(menu())

    match opcao:
        case '1':
            os.system('cls')
            valorDeposito = float(input("Informe o valor do depósito: "))
            saldo, extrato = funcao_deposito(saldo,valorDeposito,extrato)
        
        case '2':
            os.system('cls')
            print(f'\nSALDO = {saldo}\n')
            valorSaque = float(input("Informe o valor do saque: "))
            saldo, extrato, numeroSaques = funcao_saque(saldo=saldo, valorSaque=valorSaque,extrato=extrato, limite=limite, limiteSaques=limiteSaques, numeroSaques=numeroSaques)
            

        case '3':
            os.system('cls')
            mostrar_extrato(saldo,extrato=extrato)
            time.sleep(1)
        
        case '4':
            cadastrar_usuário()

        case '0':
            print("Saindo...")
            time.sleep(1)
            break
        
        case _:
            os.system('cls')
            print('Opção inválida tente novamente...')    
            time.sleep(1)
