from rich import print
from time import sleep
import os

def menu_principal():
    print(30 * '[cyan]«[/]')
    print('ESCOLHA UMA DAS AÇÕES:\n'
          '1 - ATACAR\n'
          '2 - CURAR VIDA')
    print(30 * '[cyan]»[/]')

def menu_level1():
    pass

def menu_level2():
    print('ESCOLHA A FORMA DE ATAQUE:\n'
          '1 - ATAQUE BÁSICO\n'
          '2 - HABILIDADE 1')

def menu_level3():
    print('ESCOLHA A FORMA DE ATAQUE:\n'
          '1 - ATAQUE BÁSICO\n'
          '2 - HABILIDADE 1\n'
          '3 - HABILIDADE 2')

def logo():

    for i in range(20, -1, -1):
        os.system('cls' if os.name == 'nt' else 'clear')

        print('\n' * i)
        print(r'''
        ╔════════════════════════════════════════════════════╗
        ║                                                    ║
        ║      ⚔️  GAUCHO'S ADVENTURES ⚔️                   ║
        ║                                                    ║
        ║     Peleia • Chimarrão • Pilcha • Garrucha         ║
        ║                                                    ║
        ╚════════════════════════════════════════════════════╝
        ''')

        sleep(0.1)

def carregamento():
    print('[green]Carregando[/]',end='')
    for c in range(5):
        sleep(1)
        print('.',end='')
    print('')