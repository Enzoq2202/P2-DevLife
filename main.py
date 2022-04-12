from funcoes import *
from random import *
from colorama import Fore,Style
from prettytable import PrettyTable
import unicodedata

#Fazendo uma lista com as palavras de 5 letras.
with open('palavras.txt', 'r') as arquivo:
    lista_palavras = [palavra.strip() for palavra in arquivo if len(palavra.strip()) == 5]
#Tirando o acento das palavras
lista_sem_acento = []
for palavras in lista_palavras:
    palavra_nova = normaliza_palavra(palavras)
    lista_sem_acento.append(palavra_nova)
#Variáveis
tentativas = 0
#Sorteando Palavra
palavra_sorteada = choice(lista_sem_acento)




while True:
    #Verificando se a entrada é valida
    while True:
        print(palavra_sorteada)
        pergunta_palavra = input('Digite sua chute: ')
        if verfica_palavra(pergunta_palavra) == 'Entrada Inválida':
            print(Fore.RED + 'Digite Novamente, entrada inválida' + Fore.WHITE)
        elif pergunta_palavra not in lista_sem_acento:
            print(Fore.RED + 'Digite Novamente, entrada inválida' + Fore.WHITE)
        else:
            break
    tentativas+=1
    if pergunta_palavra == palavra_sorteada:
        pergunta_ganhador = input(Fore.GREEN + f'Parabéns, você acertou em {tentativas} tentativa(s). Deseja tentar adivinhar outra palavra? [S]/[N]. ' + Fore.WHITE).upper().strip()
        if pergunta_ganhador == 'S':
            tentativas = 0
            palavra_sorteada = choice(lista_palavras)
        else:
            break
    else:
        if tentativas == 1:
            tabela_palavras = tabela_inicial(palavra_sorteada,pergunta_palavra)
            print(tabela_palavras)
        else:
            tabela_palavras = tabela_jogo(tabela_palavras,palavra_sorteada,pergunta_palavra)
            print(tabela_palavras)
    if tentativas == 6:
        pergunta_reiniciar = input(Fore.RED + f'Você Perdeu, a palavra era "{palavra_sorteada}". Deseja tentar adivinhar outra palavra? [S]/[N]. ' + Fore.WHITE).upper().strip()
        if pergunta_reiniciar == 'S':
            tentativas = 0
            palavra_sorteada = choice(lista_palavras)
        else:
            break
    
    

    
