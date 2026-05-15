
from personagens import *
from rich import print


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

def ataque():
    pass

def curar_vida():
    pass


def pensar():
    #Mecanica dos inimigos, atacar ou se curar, criar regra!
    pass

def passar_cena():
    # Printa espaço vazio (100x) quebrando as linhas, dando um efeito de 'passagem de cena'.
    print(100*' \n')

def habilidades(habil):
    #countdown de cada habilidade
    pass