from colorama import Fore
from prettytable import PrettyTable
import unicodedata
import sys
import time


#Função para printar devagar 
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)


#Criando a tabela inicial do jogo
def tabela_inicial(palavra_sorteada,palavra_chute):
    tabela_jogo = PrettyTable()
    tabela_jogo.field_names = ['1ª Letra', '2ª Letra', '3ª Letra', '4ª Letra', '5ª Letra']
    contador1 = 0
    if palavra_sorteada[0] == palavra_chute[0]:
        if palavra_sorteada[0] == palavra_chute[0] and palavra_chute.count(palavra_chute[0]) > 1:
            letra1 = Fore.GREEN + palavra_sorteada[0] + Fore.WHITE
            contador1 = 1
        else:
            letra1 = Fore.GREEN + palavra_sorteada[0] + Fore.WHITE
    elif palavra_sorteada[0] != palavra_chute[0]:
        if palavra_chute[0] in palavra_sorteada and palavra_chute.count(palavra_chute[0]) == palavra_sorteada.count(palavra_chute[0]):
            letra1 = Fore.YELLOW + palavra_chute[0] + Fore.WHITE
        elif palavra_chute[0] not in palavra_sorteada:
            letra1 = Fore.MAGENTA + palavra_chute[0] + Fore.WHITE
        elif contador1 == 0 and palavra_chute.count(palavra_chute[0]) > 1 and palavra_chute[0] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra1 = Fore.YELLOW + palavra_chute[0] + Fore.WHITE
            contador1 = 1
        elif contador1 == 1 and palavra_sorteada.count(palavra_chute[0]) > palavra_chute.count(palavra_chute[0]) and palavra_chute[0] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra1 = Fore.YELLOW + palavra_chute[0] + Fore.WHITE
            contador1 = 1
        else:
            letra1 = Fore.MAGENTA + palavra_chute[0] + Fore.WHITE
    
    if palavra_sorteada[1] == palavra_chute[1]:
        if palavra_sorteada[1] == palavra_chute[1] and palavra_chute.count(palavra_chute[1]) > 1:
            letra2 = Fore.GREEN + palavra_sorteada[1] + Fore.WHITE
            contador1 = 1
        else:
            letra2 = Fore.GREEN + palavra_sorteada[1] + Fore.WHITE
    elif palavra_sorteada[1] != palavra_chute[1]:
        if palavra_chute[1] in palavra_sorteada and palavra_chute.count(palavra_chute[1]) == palavra_sorteada.count(palavra_chute[1]):
            letra2 = Fore.YELLOW + palavra_chute[1] + Fore.WHITE
        elif palavra_chute[1] not in palavra_sorteada:
            letra2 = Fore.MAGENTA + palavra_chute[1] + Fore.WHITE
        elif contador1 == 0 and palavra_chute.count(palavra_chute[1]) > 1 and palavra_chute[1] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra2 = Fore.YELLOW + palavra_chute[1] + Fore.WHITE
            contador1 = 1
        elif contador1 == 1 and palavra_sorteada.count(palavra_chute[1]) > palavra_chute.count(palavra_chute[1]) and palavra_chute[1] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra2 = Fore.YELLOW + palavra_chute[1] + Fore.WHITE
            contador1 = 1
        else:
            letra2 = Fore.MAGENTA + palavra_chute[1] + Fore.WHITE
    
    if palavra_sorteada[2] == palavra_chute[2]:
        if palavra_sorteada[2] == palavra_chute[2] and palavra_chute.count(palavra_chute[2]) > 1:
            letra3 = Fore.GREEN + palavra_sorteada[2] + Fore.WHITE
            contador1 = 1
        else:
            letra3 = Fore.GREEN + palavra_sorteada[2] + Fore.WHITE
    elif palavra_sorteada[2] != palavra_chute[2]:
        if palavra_chute[2] in palavra_sorteada and palavra_chute.count(palavra_chute[2]) == palavra_sorteada.count(palavra_chute[2]):
            letra3 = Fore.YELLOW + palavra_chute[2] + Fore.WHITE
        elif palavra_chute[2] not in palavra_sorteada:
            letra3 = Fore.MAGENTA + palavra_chute[2] + Fore.WHITE
        elif contador1 == 0 and palavra_chute.count(palavra_chute[2]) > 1 and palavra_chute[2] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra3 = Fore.YELLOW + palavra_chute[2] + Fore.WHITE
            contador1 = 1
        elif contador1 == 1 and palavra_sorteada.count(palavra_chute[2]) > palavra_chute.count(palavra_chute[2]) and palavra_chute[2] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra3 = Fore.YELLOW + palavra_chute[2] + Fore.WHITE
            contador1 = 1
        else:
            letra3 = Fore.MAGENTA + palavra_chute[2] + Fore.WHITE
    
    if palavra_sorteada[3] == palavra_chute[3]:
        if palavra_sorteada[3] == palavra_chute[3] and palavra_chute.count(palavra_chute[3]) > 1:
            letra4 = Fore.GREEN + palavra_sorteada[3] + Fore.WHITE
            contador1 = 1
        else:
            letra4 = Fore.GREEN + palavra_sorteada[3] + Fore.WHITE
    elif palavra_sorteada[3] != palavra_chute[3]:
        if palavra_chute[3] in palavra_sorteada and palavra_chute.count(palavra_chute[3]) == palavra_sorteada.count(palavra_chute[3]):
            letra4 = Fore.YELLOW + palavra_chute[3] + Fore.WHITE
        elif palavra_chute[3] not in palavra_sorteada:
            letra4 = Fore.MAGENTA + palavra_chute[3] + Fore.WHITE
        elif contador1 == 0 and palavra_chute.count(palavra_chute[3]) > 1 and palavra_chute[3] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra4 = Fore.YELLOW + palavra_chute[3] + Fore.WHITE
            contador1 = 1
        elif contador1 == 1 and palavra_sorteada.count(palavra_chute[3]) > palavra_chute.count(palavra_chute[3]) and palavra_chute[3] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra4 = Fore.YELLOW + palavra_chute[3] + Fore.WHITE
            contador1 = 1
        else:
            letra4 = Fore.MAGENTA + palavra_chute[3] + Fore.WHITE
    
    if palavra_sorteada[4] == palavra_chute[4]:
        if palavra_sorteada[4] == palavra_chute[4] and palavra_chute.count(palavra_chute[4]) > 1:
            letra5 = Fore.GREEN + palavra_sorteada[4] + Fore.WHITE
            contador1 = 1
        else:
            letra5 = Fore.GREEN + palavra_sorteada[4] + Fore.WHITE
    elif palavra_sorteada[4] != palavra_chute[4]:
        if palavra_chute[4] in palavra_sorteada and palavra_chute.count(palavra_chute[4]) == palavra_sorteada.count(palavra_chute[4]):
            letra5 = Fore.YELLOW + palavra_chute[4] + Fore.WHITE
        elif palavra_chute[4] not in palavra_sorteada:
            letra5 = Fore.MAGENTA + palavra_chute[4] + Fore.WHITE
        elif contador1 == 0 and palavra_chute.count(palavra_chute[4]) > 1 and palavra_chute[4] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra5 = Fore.YELLOW + palavra_chute[4] + Fore.WHITE
            contador1 = 1
        elif contador1 == 1 and palavra_sorteada.count(palavra_chute[4]) > palavra_chute.count(palavra_chute[4]) and palavra_chute[4] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra5 = Fore.YELLOW + palavra_chute[4] + Fore.WHITE
            contador1 = 1
        else:
            letra5 = Fore.MAGENTA + palavra_chute[4] + Fore.WHITE
    
    tabela_jogo.add_row([letra1,letra2,letra3,letra4,letra5])
    return tabela_jogo

#Criando a tabela que será atualizada com as novas palavras
def tabela_jogo(tabela,palavra_sorteada,palavra_chute):
    contador1 = 0
    if palavra_sorteada[0] == palavra_chute[0]:
        if palavra_sorteada[0] == palavra_chute[0] and palavra_chute.count(palavra_chute[0]) > 1:
            letra1 = Fore.GREEN + palavra_sorteada[0] + Fore.WHITE
            contador1 = 1
        else:
            letra1 = Fore.GREEN + palavra_sorteada[0] + Fore.WHITE
    elif palavra_sorteada[0] != palavra_chute[0]:
        if palavra_chute[0] in palavra_sorteada and palavra_chute.count(palavra_chute[0]) == palavra_sorteada.count(palavra_chute[0]):
            letra1 = Fore.YELLOW + palavra_chute[0] + Fore.WHITE
        elif palavra_chute[0] not in palavra_sorteada:
            letra1 = Fore.MAGENTA + palavra_chute[0] + Fore.WHITE
        elif contador1 == 0 and palavra_chute.count(palavra_chute[0]) > 1 and palavra_chute[0] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra1 = Fore.YELLOW + palavra_chute[0] + Fore.WHITE
            contador1 = 1
        elif contador1 == 1 and palavra_sorteada.count(palavra_chute[0]) > palavra_chute.count(palavra_chute[0]) and palavra_chute[0] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra1 = Fore.YELLOW + palavra_chute[0] + Fore.WHITE
            contador1 = 1
        else:
            letra1 = Fore.MAGENTA + palavra_chute[0] + Fore.WHITE
    
    if palavra_sorteada[1] == palavra_chute[1]:
        if palavra_sorteada[1] == palavra_chute[1] and palavra_chute.count(palavra_chute[1]) > 1:
            letra2 = Fore.GREEN + palavra_sorteada[1] + Fore.WHITE
            contador1 = 1
        else:
            letra2 = Fore.GREEN + palavra_sorteada[1] + Fore.WHITE
    elif palavra_sorteada[1] != palavra_chute[1]:
        if palavra_chute[1] in palavra_sorteada and palavra_chute.count(palavra_chute[1]) == palavra_sorteada.count(palavra_chute[1]):
            letra2 = Fore.YELLOW + palavra_chute[1] + Fore.WHITE
        elif palavra_chute[1] not in palavra_sorteada:
            letra2 = Fore.MAGENTA + palavra_chute[1] + Fore.WHITE
        elif contador1 == 0 and palavra_chute.count(palavra_chute[1]) > 1 and palavra_chute[1] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra2 = Fore.YELLOW + palavra_chute[1] + Fore.WHITE
            contador1 = 1
        elif contador1 == 1 and palavra_sorteada.count(palavra_chute[1]) > palavra_chute.count(palavra_chute[1]) and palavra_chute[1] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra2 = Fore.YELLOW + palavra_chute[1] + Fore.WHITE
            contador1 = 1
        else:
            letra2 = Fore.MAGENTA + palavra_chute[1] + Fore.WHITE
    
    if palavra_sorteada[2] == palavra_chute[2]:
        if palavra_sorteada[2] == palavra_chute[2] and palavra_chute.count(palavra_chute[2]) > 1:
            letra3 = Fore.GREEN + palavra_sorteada[2] + Fore.WHITE
            contador1 = 1
        else:
            letra3 = Fore.GREEN + palavra_sorteada[2] + Fore.WHITE
    elif palavra_sorteada[2] != palavra_chute[2]:
        if palavra_chute[2] in palavra_sorteada and palavra_chute.count(palavra_chute[2]) == palavra_sorteada.count(palavra_chute[2]):
            letra3 = Fore.YELLOW + palavra_chute[2] + Fore.WHITE
        elif palavra_chute[2] not in palavra_sorteada:
            letra3 = Fore.MAGENTA + palavra_chute[2] + Fore.WHITE
        elif contador1 == 0 and palavra_chute.count(palavra_chute[2]) > 1 and palavra_chute[2] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra3 = Fore.YELLOW + palavra_chute[2] + Fore.WHITE
            contador1 = 1
        elif contador1 == 1 and palavra_sorteada.count(palavra_chute[2]) > palavra_chute.count(palavra_chute[2]) and palavra_chute[2] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra3 = Fore.YELLOW + palavra_chute[2] + Fore.WHITE
            contador1 = 1
        else:
            letra3 = Fore.MAGENTA + palavra_chute[2] + Fore.WHITE
    
    if palavra_sorteada[3] == palavra_chute[3]:
        if palavra_sorteada[3] == palavra_chute[3] and palavra_chute.count(palavra_chute[3]) > 1:
            letra4 = Fore.GREEN + palavra_sorteada[3] + Fore.WHITE
            contador1 = 1
        else:
            letra4 = Fore.GREEN + palavra_sorteada[3] + Fore.WHITE
    elif palavra_sorteada[3] != palavra_chute[3]:
        if palavra_chute[3] in palavra_sorteada and palavra_chute.count(palavra_chute[3]) == palavra_sorteada.count(palavra_chute[3]):
            letra4 = Fore.YELLOW + palavra_chute[3] + Fore.WHITE
        elif palavra_chute[3] not in palavra_sorteada:
            letra4 = Fore.MAGENTA + palavra_chute[3] + Fore.WHITE
        elif contador1 == 0 and palavra_chute.count(palavra_chute[3]) > 1 and palavra_chute[3] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra4 = Fore.YELLOW + palavra_chute[3] + Fore.WHITE
            contador1 = 1
        elif contador1 == 1 and palavra_sorteada.count(palavra_chute[3]) > palavra_chute.count(palavra_chute[3]) and palavra_chute[3] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra4 = Fore.YELLOW + palavra_chute[3] + Fore.WHITE
            contador1 = 1
        else:
            letra4 = Fore.MAGENTA + palavra_chute[3] + Fore.WHITE
    
    if palavra_sorteada[4] == palavra_chute[4]:
        if palavra_sorteada[4] == palavra_chute[4] and palavra_chute.count(palavra_chute[4]) > 1:
            letra5 = Fore.GREEN + palavra_sorteada[4] + Fore.WHITE
            contador1 = 1
        else:
            letra5 = Fore.GREEN + palavra_sorteada[4] + Fore.WHITE
    elif palavra_sorteada[4] != palavra_chute[4]:
        if palavra_chute[4] in palavra_sorteada and palavra_chute.count(palavra_chute[4]) == palavra_sorteada.count(palavra_chute[4]):
            letra5 = Fore.YELLOW + palavra_chute[4] + Fore.WHITE
        elif palavra_chute[4] not in palavra_sorteada:
            letra5 = Fore.MAGENTA + palavra_chute[4] + Fore.WHITE
        elif contador1 == 0 and palavra_chute.count(palavra_chute[4]) > 1 and palavra_chute[4] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra5 = Fore.YELLOW + palavra_chute[4] + Fore.WHITE
            contador1 = 1
        elif contador1 == 1 and palavra_sorteada.count(palavra_chute[4]) > palavra_chute.count(palavra_chute[4]) and palavra_chute[4] in palavra_sorteada and palavra_chute[0] != palavra_sorteada[0]:
            letra5 = Fore.YELLOW + palavra_chute[4] + Fore.WHITE
            contador1 = 1
        else:
            letra5 = Fore.MAGENTA + palavra_chute[4] + Fore.WHITE
    
    
    tabela.add_row([letra1,letra2,letra3,letra4,letra5])
    return tabela

#Função que remove acentos
def remove_acentos(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

#Funcao que escreve as palavras sem acento
def normaliza_palavra(palavra):
    palavra = palavra.lower()
    str_final = ''
    for letra in palavra:
        str_final += remove_acentos(letra)
    return str_final

#Função que tira o acento da palavra e coloca em uma lista nova
def lista_sem_acento(lista_palavras):
    lista_sem_acento = []
    for palavras in lista_palavras:
        palavra_nova = normaliza_palavra(palavras)
        lista_sem_acento.append(palavra_nova)
    return lista_sem_acento

#Função que verifica o input, caso a pessoa coloque alguma entrada que seja inválida
def verfica_palavra(palavra):
    for letra in palavra.strip():
        letra = remove_acentos(letra)
        if letra not in "abcdefghijklmnopqrstuvwxyz" or len(palavra.strip()) != 5:
            return 'Entrada Inválida'
    return palavra.strip()

#Função para atulizar o dicionário com as cores das letras
def teclado(palavra_sorteada,palavra_chute,dicionario):
    for i in range(5):
        if palavra_chute[i] not in palavra_sorteada:
            dicionario[palavra_chute[i]] = 'magenta'
        elif palavra_chute[i] in palavra_sorteada and palavra_chute[i] == palavra_sorteada[i]:
            dicionario[palavra_chute[i]] = 'verde'
        else:
            dicionario[palavra_chute[i]] = 'amarelo'
    return dicionario

#Função que vai pintar as letras do teclado
def pinta_teclado(dicionario):
    lista_teclado = []
    for letras in dicionario:
        if dicionario[letras] == 'verde':
            lista_teclado.append(Fore.GREEN + letras)
        elif dicionario[letras] == 'amarelo':
            lista_teclado.append(Fore.YELLOW + letras)
        elif dicionario[letras] == 'magenta':
            lista_teclado.append(Fore.MAGENTA + letras)
        else:
            lista_teclado.append(Fore.BLACK + letras + Fore.WHITE)
    return lista_teclado
