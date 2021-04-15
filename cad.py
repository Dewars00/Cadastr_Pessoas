from os import system
from time import sleep
import factor

pessoas = []
dados = {}
index = 0
vf = False
delete = 0
opt = ''
v = ''

system('cls')
factor.topo('SISTEMA DE CADASTRO DE PESSOAS')
input('Aperte ENTER para iniciar...')

while True:
    opt = factor.menu(opt)
    system('cls')
    sleep(1)
    if opt == 1:
        while True:
            factor.topo('CADASTRO')
            if len(pessoas) > 0:
                index = pessoas[-1]['ID '] +1
            dados['ID '] = index
            dados['Nome'] = str(input('Nome: ')).upper()
            dados['Idade'] = int(input('Idade: '))
            x = str(input('Sexo[M/F]: ')).upper()       
            dados['Sexo'] = factor.SexoVerificacao(x)
            pessoas.append(dados.copy())
            dados.clear()
            v = factor.DesejaContinuar(v)      
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
            sleep(0.001)
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
                v = factor.DesejaContinuar(v)
            sleep(1)
            system('cls')
            if v == 'N':
                break
    elif opt == 4:
            factor.topo('GERAR ARQUIVO')
            print('Essa opção irá criar um arquivo com todos os cadastros\ne em seguida encerrará o programa!!\n')
            v = factor.DesejaContinuar(v)
            if v == 'S':
                arq = open("Cadastros.txt", "w")
                arq.write('='*60)
                arq.write('\n')
                arq.write(f'{"PESSOAS CADASTRADAS"}'.center(60))
                arq.write('\n')
                arq.write('='*60)
                for i in range (0,len(pessoas)):
                    arq.write('\n\n')
                    arq.write('='*60)
                    for k,v in pessoas[i].items():
                        arq.write(f'\n{k} \t ====== \t{v}')
                    arq.write('\n')
                    arq.write('='*60)
                arq.write('\n')
                arq.close()
                opt = 5
                sleep(1)
                system('cls')
                break
    if opt == 5:
        break
factor.topo('FINALIZANDO')
print('ATÉ MAIS!!!')
input()
