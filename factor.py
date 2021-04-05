def SexoVerificacao(x):
    from time import sleep
    while True:
        if x in 'MF':
            break
        else:
            print('===Entre com um valor válido!===')
            sleep(1)
            x = str(input('Sexo[M/F]: ')).upper()

    
def DesejaContinuar(v):
    from time import sleep
    while True:
        if v in 'SN':
            break
        else:
            print('===Entre com um valor válido!===')
            sleep(1)
            v = str(input('Deseja continuar[S/N]? ')).upper()

        
