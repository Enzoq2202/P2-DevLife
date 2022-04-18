from funcoes import *
from random import *
from colorama import Fore,Style
from prettytable import PrettyTable
import unicodedata
import sys

#Fazendo uma lista com as palavras de 5 letras.
with open('palavras.txt', 'r') as arquivo:
    lista_palavras = [palavra.strip() for palavra in arquivo if len(palavra.strip()) == 5]
#Tirando o acento das palavras e colocando em uma lista
lista_palavra_formatada = lista_sem_acento(lista_palavras)
#Variáveis
tentativas = 0
tentativas_acerto = 'acertou'
contador_partidas = 0
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
dic_tentativas = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    'Não acertou':0
}
#Sorteando Palavra
palavra_sorteada = choice(lista_palavra_formatada)


#Tutorial
while True:
    pergunta_tutorial = input('Deseja ler o tutorial do jogo? [S]/[N]. ').lower().strip()
    if pergunta_tutorial == 's':
        print('Tente acertar a palavra sorteada em até 6 tentativas. O jogo sempre informará a situação em que o jogador se encontra.\nCaso a palavra escrita pelo jogador possua alguma letra ' + Fore.GREEN + 'dessa cor ' + Fore.WHITE +', significa que a letra está presente na palavra e se encontra na posição correta.\nCaso seja ' + Fore.YELLOW + 'dessa cor ' + Fore.WHITE + ', significa que a letra está presente na palavra, porém não se encontra na posição correta.\nE por fim, caso seja ' + Fore.MAGENTA + 'dessa cor ' + Fore.WHITE + ', significa que a letra não está presente na palavra.')
        break
    elif pergunta_tutorial == 'n':
        break
    else:
        print(Fore.RED + 'Entrada inválida.' + Fore.WHITE)


#Início do jogo
while True:
    #Verificando se a entrada é valida
    while True:
        print('\n')
        pergunta_palavra = remove_acentos(input('Digite seu chute: ').lower().strip())
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
            teclado_dic = teclado(palavra_sorteada,pergunta_palavra,dic_teclado)
            teclado_pintado = pinta_teclado(teclado_dic)
            for elem in teclado_pintado:
                sys.stdout.write(elem + '     ')
        else:
            tabela_palavras = tabela_jogo(tabela_palavras,palavra_sorteada,pergunta_palavra)
            print(tabela_palavras)
        print('\n')   
        pergunta_ganhador = input(Fore.GREEN + f'Parabéns, você acertou em {tentativas} tentativa(s). Deseja tentar adivinhar outra palavra? [S]/[N]. ' + Fore.WHITE).upper().strip()
        if pergunta_ganhador == 'S':
            dic_tentativas = resumo_rodadas(dic_tentativas,tentativas,tentativas_acerto)
            tentativas = 0
            palavra_sorteada = choice(lista_palavra_formatada)
            contador_partidas+=1
        else:
            dic_tentativas = resumo_rodadas(dic_tentativas,tentativas,tentativas_acerto)
            contador_partidas+=1
            break
    else:
        if tentativas == 1:
            tabela_palavras = tabela_inicial(palavra_sorteada,pergunta_palavra)
            print(tabela_palavras)
            teclado_dic = teclado(palavra_sorteada,pergunta_palavra,dic_teclado)
            teclado_pintado = pinta_teclado(teclado_dic)
            for elem in teclado_pintado:
                sys.stdout.write(elem + '     ')
        else:
            tabela_palavras = tabela_jogo(tabela_palavras,palavra_sorteada,pergunta_palavra)
            print(tabela_palavras)
            teclado_dic = teclado(palavra_sorteada,pergunta_palavra,dic_teclado)
            teclado_pintado = pinta_teclado(teclado_dic)
            for elem in teclado_pintado:
                sys.stdout.write(elem + '     ')
    if tentativas == 6:
        print('\n')
        pergunta_reiniciar = input(Fore.RED + f'Você Perdeu, a palavra era "{palavra_sorteada}". Deseja tentar adivinhar outra palavra? [S]/[N]. ' + Fore.WHITE).upper().strip()
        if pergunta_reiniciar == 'S':
            tentativas = 0
            tentativas_acerto = 'Não acertou'
            dic_tentativas = resumo_rodadas(dic_tentativas,tentativas,tentativas_acerto)
            palavra_sorteada = choice(lista_palavra_formatada)
            tentativas_acerto = 'acertou'
            contador_partidas+=1
        else:
            tentativas = 0
            tentativas_acerto = 'Não acertou'
            dic_tentativas = resumo_rodadas(dic_tentativas,tentativas,tentativas_acerto)
            contador_partidas+=1
            break

resumao = porcentagem_final(dic_tentativas,contador_partidas)
for elem,valor in resumao.items():
    print(Fore.CYAN + elem,':',valor,'%')