from os import system
from time import sleep
import factor

pessoas = []
dados = {}
v = 's'

system('cls')
print('=====Sistema para cadastro de pessoas=====')
print()
input('Aperte ENTER para iniciar...')
system('cls')
sleep(1)

while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Idade'] = int(input('Idade: '))
    x = str(input('Sexo[M/F]: ')).upper()
    factor.SexoVerificacao(x)       
    dados['Sexo'] = x
    pessoas.append(dados.copy())
    dados.clear()
    v = str(input('Deseja continuar[S/N]? ')).upper()
    factor.DesejaContinuar(v)      
    sleep(1)
    system('cls')
    if v == 'N':
        break

for i in range (0,len(pessoas)):
    print('=' * 60)
    for k,v in pessoas[i].items():
        print(f'{k} \t====== \t{v}')
    print('=' * 60)
    print()


