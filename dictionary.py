import os

os.system('cls')

dicionario = {'nome' : 'Enzo',
                'idade' : 18,
                'altura':1.87 }

dicionario ['Dev'] = True

for i in dicionario:
    print(f'{i} = {dicionario[i]}')