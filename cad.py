from os import system
from time import sleep
import factor

pessoas = []
dados = {}
v = 's'

system('cls')
factor.topo('SISTEMA DE CADASTRO DE PESSOAS')
input('Aperte ENTER para iniciar...')
opt = factor.menu()
system('cls')
sleep(1)
if opt == 1:
    while True:
        factor.topo('SISTEMA DE CADASTRO DE PESSOAS')
        dados['Nome'] = str(input('Nome: ')).upper()
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
elif opt == 2:
    factor.topo('PESSOAS CADASTRADAS')
    for i in range (0,len(pessoas)):
        print('=' * 60)
        for k,v in pessoas[i].items():
            print(f'{k} \t====== \t{v}')
        print('=' * 60)
        print()


