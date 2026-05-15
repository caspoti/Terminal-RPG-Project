from rich import print

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