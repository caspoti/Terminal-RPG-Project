from personagens import *
from mecanicas import *
from menus import *
from rich import print
from rich.panel import Panel
from time import sleep

# criar inimigos dentro de cada level

# colocar os elos dentro dos LEVELS, pois antes de iniciar o level, o personagem ganha uma habilidade nova
# sem precisar executar funcoes de elo ou habilidade, assim como o inimigo que já vem com a habilidade criada
def elo_1(player):
    pass
def elo_2():
    # Criar lista com habilidades
    # A ideia é: player.habilidade.append('habilidade especial')
    pass
def elo_3():
    pass

def painel_level1(player,cpu): # informacoes dos personagens
    inimigo = Panel(f'[yellow]Força: {cpu.forca} atk\nVida: {cpu.vida} HP\n'
                  'Habilidades: N/A[/]', title=f'{cpu.nome}', style='red', width=30)
    player = Panel(f'[yellow]Força: {player.forca} atk\nVida: {player.vida} HP\n'
                  'Habilidades: N/A[/]', title=f'{player.nome}({player.__class__.__name__})', style='red', width=30)
    print(inimigo,player)

def level_1(player):
    # Aqui ira acontecer a batalha contra o primeiro boss
    cpu = BestaCauda()
    rodada = 0
    ataques = 0
    while True:
        if rodada % 2 == 0:
            sleep(2)
            painel_level1(player,cpu)
            sleep(1)
            menu_principal() # 1- ataque,2- curar
            escolha = int(input('Digite o número: '))
            if escolha == 1:
                atk = player.atacar(player.forca)
                if atk is not None:
                    print(60 * '[green]-[/]')
                    print(f'{player.nome} acertou {cpu.nome} com {player.habilidade[0]} de {atk:.0f} força')
                    sleep(1)
                    print(cpu.receber_dano(atk))
                    print(60 * '[green]-[/]')
                    sleep(1)
                    print(player.nome, player.vida, player.forca)
                    print(cpu.vida)
                    vivo = cpu.conferir_vida()
                    if vivo is not True:
                        break
                else:
                    print(50 * '[red]-[/]')
                    print(f'{player.nome} errou o ataque!')
                    print(50 * '[red]-[/]')
                    sleep(1)
            elif escolha == 2:
                cura = player.curar
                print(cura)

            #mecanica do player
            # se jogador acerta o ataque - ataques += 1
            # se errar o ataque - ataque = 0
            rodada += 1
        else:
            rodada += 1
            #mecanica do CPU
        # rodada define a vez de quem jogar(par para player/ impar para CPU)
        # ataques vai definir quando o inimigo deve usar o curar(RECEBER 2 ATAQUES CONSECUTIVOS)
    print(f'[green]PARABENS {player.nome}! Você derrotou[/] [red]{cpu.nome}[/][green] e passou para '
          f'próximo nivel[/]')