from personagens import *
from rich import print
from time import sleep
import os

wizard = Mago()
warrior = Guerreiro()
archer = Arqueiro()
def criar_personagem():
    print(80*'[green]-[/]','\n')
    print('[green]ESCOLHA SEU PERSONAGEM:[/]'.center(80))
    print(80 * '[green]-[/]')
    art1 = r"""
           01
         __/\__
    . _  \\''//
    -( )-/_||_\
     .'. \_()_/
      |   | . \
      |   | .  \
     .'. ,\_____'.
    """

    art2 = r"""
               02
     _   _   _   _+       |
    /_`-'_`-'_`-'_|  \+/  |
    \_`M'_`D'_`C'_| _<=>_ |
      `-' `-' `-' 0/ \ / o=o
                  \/\ ^ /`0
                  | /_^_\
                  | || ||
                __|_d|_|b__
    """

    art3 = r"""
             03
           /|   \
            /_|_{)/
    ---<<   | |  )
            \ |  (
             \|  )
                /|
                \ \
                ~ ~
    """

    # split em linhas
    a1 = art1.splitlines()
    a2 = art2.splitlines()
    a3 = art3.splitlines()

    # iguala tamanho
    max_len = max(len(a1), len(a2), len(a3))
    a1 += [""] * (max_len - len(a1))
    a2 += [""] * (max_len - len(a2))
    a3 += [""] * (max_len - len(a3))

    # imprime lado a lado
    for l1, l2, l3 in zip(a1, a2, a3):
        print(l1.ljust(16) + l2.ljust(25) + l3)
    print(8*' ','MAGO',17*' ','GUERREIRO',15*' ','ARQUEIRO')
    print(2*' ','ATK:',wizard.forca,'  HP:', wizard.vida,
          4*' ','ATK:',warrior.forca,'  HP:', warrior.vida,
          6*' ','ATK:',archer.forca,'  HP:',archer.vida)
    print(80 * '[green]-[/]','\n')
    escolha = int(input('Digite o número do personagem: '))
    print(80 * '[green]-[/]')
    if escolha == 1:
        name = str(input('Digite o nome do personagem: ').strip().title())
        print(80 * '[green]-[/]')
        p1 = Mago(name)
    elif escolha == 2:
        name = str(input('Digite o nome do personagem: ').strip().title())
        print(80 * '[green]-[/]')
        p1 = Guerreiro(name)
    elif escolha == 3:
        name = str(input('Digite o nome do personagem: ').strip().title())
        print(80 * '[green]-[/]')
        p1 = Arqueiro(name)
    return p1

def ataque(player,cpu):
    atk = player.atacar(player.forca)
    if atk is not None:
        print(60 * '[green]-[/]')
        print(f'{player.nome} acertou {cpu.nome} com {player.habilidade[0]} de {atk:.0f} força')
        sleep(1)
        print(cpu.receber_dano(atk))
        print(60 * '[green]-[/]')
        sleep(1)
    else:
        print(50 * '[red]-[/]')
        print(f'{player.nome} errou o ataque!')
        print(50 * '[red]-[/]')
        sleep(1)

def curar_vida(player):
    cura = player.curar()
    if cura is not None:
        print(50 * '[blue]-[/]')
        print(f'{player.nome} curou {cura} HP')
        print(50 * '[blue]-[/]')
        return 1 # PARA PASSAR A RODADA
    else:
        print(50 * '[red]-[/]')
        print('Você já está com o máximo de vida!')
        print(50 * '[red]-[/]')
        return 0 # NÃO PASSAR A RODADA, POIS A CURA NAO FOI USADA


def pensar():
    #Mecanica dos inimigos, atacar ou se curar, criar regra!
    pass

def limpar_tela(tempo = 0):
    # limpa o terminal
    sleep(tempo)
    os.system('cls' if os.name == 'nt' else 'clear')

def habilidades(habil):
    #countdown de cada habilidade
    pass