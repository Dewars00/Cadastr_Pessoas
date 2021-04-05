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
    factor.SexoVerificacao(x)       #! Função que verifica se o valor inserido para sexo é válido
    dados['Sexo'] = x
    pessoas.append(dados.copy())
    dados.clear()
    v = str(input('Deseja continuar[S/N]? ')).upper()
    factor.DesejaContinuar(v)       #! Função que verifica se o valor de v é válido
    sleep(1)
    system('cls')
    if v == 'N':
        break



print(pessoas)

