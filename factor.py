from time import sleep
from os import system


def SexoVerificacao(x):    #! Função que verifica se o valor inserido para sexo é válido
    if x not in 'MF':
        while True:
            if x in 'MF':
                break
            print('===Entre com um valor válido!===')
            sleep(1)
            x = str(input('Sexo[M/F]: ')).upper()
    return x

    
def DesejaContinuar(v):    #! Função que verifica se o valor de v é válido
    v = str(input('Deseja continuar[S/N]? ')).upper()
    while True:
        if v in 'SN':
            break
        print(f'ERRO! ENTRE COM UM VALOR VÁLIDO')
        sleep(1)
        v = str(input('Deseja continuar[S/N]? ')).upper()
    return v

        
def topo(msg):      #! Mensagem do topo da tela
    print('='*60)
    print(f'{msg}'.center(60))
    print('='*60)
    print()

    

def menu(num):     #!Função para a tela de menu
    sleep(1)
    system('cls')
    topo('MENU PRINCIPAL')
    print('[1] NOVO CADASTRO\n[2] EXIBIR TODOS OS CADASTROS\n[3] EXCLUIR UM CADASTRO\n[4] SAIR')
    opt = str(input('\nESCOLHA UMA DAS OPÇÕES DO MENU... '))
    while True:
        if opt in '1234':
            break
        print('ERRO!!! Entre com um valor válido!')
        sleep(1.5)
        opt = str(input('\nESCOLHA UMA DAS OPÇÕES DO MENU... '))
    ret = int(opt)
    return ret
    
    

    