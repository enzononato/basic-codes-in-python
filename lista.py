import os

os.system('cls')



print('Insira suas notas maiores ou iguais a 0 e menores ou iguais a 10: (para sair encerrar basta colocar uma nota abaixo de 0 ou acima de 10)')
notas = [0]


while notas[len(notas)-1] <= 10 and notas[len(notas)-1] >= 0:
    notas.append(float(input()))
    if notas[-1] > 10 or notas[-1] < 0:
        notas.pop()
        break
os.system("cls")

media = sum(notas)/(len(notas)-1)

print('Média:', round(media,2))
