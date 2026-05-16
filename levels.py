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
            print(f'[cyan]============[/][blue] Rodada: {rodada} [/][cyan]============[/]')
            painel_level1(player,cpu)
            sleep(1)
            menu_principal() # 1- ataque,2- curar
            escolha = int(input('Digite o número: '))
            if escolha == 1: # OPCAO DE ATAQUE DO PLAYER
                ataque(player,cpu)
                vivo = cpu.conferir_vida()
                if vivo is not True:
                    break
                rodada += 1
            elif escolha == 2: # OPCAO DE CURA DO PLAYER
                limpar_tela(1)
                rodada += curar_vida(player)
            #mecanica do player
            # se jogador acerta o ataque - ataques += 1
            # se errar o ataque - ataque = 0
        else:
            rodada += 1
            #mecanica do CPU
        # rodada define a vez de quem jogar(par para player/ impar para CPU)
        # ataques vai definir quando o inimigo deve usar o curar(RECEBER 2 ATAQUES CONSECUTIVOS)
    print(f'[green]PARABENS {player.nome}! Você derrotou[/] [red]{cpu.nome}[/][green] e passou para '
          f'próximo nivel[/]')