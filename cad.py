from os import system
from time import sleep
import factor

pessoas = []
dados = {}
v = 's'
index = 0
vf = False
delete = 0

system('cls')
factor.topo('SISTEMA DE CADASTRO DE PESSOAS')
input('Aperte ENTER para iniciar...')

while True:
    opt = factor.menu()
    system('cls')
    sleep(1)
    if opt == 1:
        while True:
            factor.topo('CADASTRO')
            if len(pessoas) > 0:
                index = pessoas[-1]['ID'] +1
            dados['ID'] = index
            dados['Nome'] = str(input('Nome: ')).upper()
            dados['Idade'] = int(input('Idade: '))
            x = str(input('Sexo[M/F]: ')).upper()       
            dados['Sexo'] = factor.SexoVerificacao(x)
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
        input('\nAperte ENTER para continuar...')
    elif opt == 3:
        while True:
            factor.topo('EXCLUIR CADASTRO')
            ex = int(input('Entre com o ID do cadastro que deseja excluir: '))
            for i in range (0,len(pessoas)):
                if pessoas[i]['ID'] == ex:
                    delete = i
                    vf = True
            if vf == True:
                del pessoas[delete]
                print('Cadastro excluído com sucesso!')
            else:
                print('ID não encontrado, tente novamente!')
                sleep(1)
                v = str=(input('Deseja continuar? [S/N]'))
                factor.DesejaContinuar(v)
            if vf == True or v == 'S':
                break






