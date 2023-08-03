import os

os.system('cls')

def calculadora(num1, num2, operador):
    match operador:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*' | 'x' | 'X':
            return num1 * num2
        case '/':
            return num1 / num2
        case _:
            return 'operação inválida'


print ("Escolha 2 números:")
n1 = float(input())
n2 = float(input())
print("Agora escolha a operação desejada: ")
operacao = str(input())

os.system('cls')

print(f"RESULTADO\n\n{n1} {operacao} {n2} = {round(calculadora(n1,n2,operacao),2)}")