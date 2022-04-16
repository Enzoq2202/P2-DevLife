from funcoes import *
from random import *
from colorama import Fore,Style
from prettytable import PrettyTable
import unicodedata

#Fazendo uma lista com as palavras de 5 letras.
with open('palavras.txt', 'r', encoding="utf-8") as arquivo:
    lista_palavras = [palavra.strip() for palavra in arquivo if len(palavra.strip()) == 5]
#Tirando o acento das palavras e colocando em uma lista
lista_palavra_formatada = lista_sem_acento(lista_palavras)
#Variáveis
tentativas = 0
dic_teclado = {
    'a':'none',
    'b':'none',
    'c':'none',
    'd':'none',
    'e':'none',
    'f':'none',
    'g':'none',
    'h':'none',
    'i':'none',
    'j':'none',
    'k':'none',
    'l':'none',
    'm':'none',
    'n':'none',
    'o':'none',
    'p':'none',
    'q':'none',
    'r':'none',
    's':'none',
    't':'none',
    'u':'none',
    'v':'none',
    'w':'none',
    'x':'none',
    'y':'none',
    'z':'none',
}
#Sorteando Palavra
palavra_sorteada = choice(lista_palavra_formatada)

#Início do jogo
while True:
    #Verificando se a entrada é valida
    while True:
        pergunta_palavra = remove_acentos(input('Digite sua chute: ').lower().strip())
        if verfica_palavra(pergunta_palavra) == 'Entrada Inválida':
            print(Fore.RED + 'Digite Novamente, entrada inválida' + Fore.WHITE)
        elif pergunta_palavra not in lista_palavra_formatada:
            print(Fore.RED + 'Digite Novamente, entrada inválida' + Fore.WHITE)
        else:
            break
    tentativas+=1
    if pergunta_palavra == palavra_sorteada:
        if tentativas == 1:
            tabela_palavras = tabela_inicial(palavra_sorteada,pergunta_palavra)
            print(tabela_palavras)
        else:
            tabela_palavras = tabela_jogo(tabela_palavras,palavra_sorteada,pergunta_palavra)
            print(tabela_palavras)   
        pergunta_ganhador = input(Fore.GREEN + f'Parabéns, você acertou em {tentativas} tentativa(s). Deseja tentar adivinhar outra palavra? [S]/[N]. ' + Fore.WHITE).upper().strip()
        if pergunta_ganhador == 'S':
            tentativas = 0
            palavra_sorteada = choice(lista_palavra_formatada)
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
            palavra_sorteada = choice(lista_palavra_formatada)
        else:
            break
    
    

    
