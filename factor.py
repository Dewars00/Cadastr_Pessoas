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
    while True:
        if v in 'SN':
            break
        print(f'ERRO! ENTRE COM UM VALOR VÁLIDO')
        sleep(1)
        v = str(input('Deseja continuar[S/N]? ')).upper()

        
def topo(msg):      #! Mensagem do topo da tela
    print('='*60)
    print(f'{msg}'.center(60))
    print('='*60)
    print()


def notint(num):
    while True:
        if num in '1234':
                break
        sleep(1)
        print()
        print('ERRO! ENTRE COM UM VALOR VÁLIDO')
        sleep(1)
        menu()
    if num.isnumeric():
        x = int(num)
    return x


def menu():
    sleep(1)
    system('cls')
    topo('MENU PRINCIPAL')
    print('[1] NOVO CADASTRO\n[2] EXIBIR TODOS OS CADASTROS\n[3] EXCLUIR UM CADASTRO\n[4] SAIR')
    print()
    opt = str(input('ESCOLHA UMA DAS OPÇÕES ACIMA... '))
    opt = notint(opt)
    return opt
    sleep(1)