from personagens import *
from rich import print, inspect
from mecanicas import *
from levels import *

def main():
    player = criar_personagem()
    level_1(player) #--- o jogo vai rodar dentro do level 1, onde vai criar o personagem cpu = BESTACAUDA()
    # level_2(player) #--- o jogo vai rodar dentro do level 2, onde vai criar o personagem cpu = CAO()
    # level_3(player) #--- o jogo vai rodar dentro do level 3, onde vai criar o personagem cpu = CAPIVARA MONSTRO()
    cpu = CAO()
    #print(cpu.habilidade(player))
    #atk = player.atacar(player.forca)
    #if atk is not None:
    #    print(f'{player.nome} acertou {cpu.nome} com {player.habilidade[0]} de {atk:.0f} força')
    #    print(cpu.receber_dano(atk))
    #    print(player.nome, player.vida, player.forca)
    #    print(cpu.vida)
    #else:
    #    print(f'{player.nome} errou o ataque!')
    # a mecanica escrita acima, vai passar para dentro de cada level


if __name__ == '__main__':
    main()

