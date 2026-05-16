from abc import ABC, abstractmethod
from random import randint


def rolar_dados(lados):
    import time
    import os

    # animação do dado
    for i in range(15):
        numero = randint(1, lados)

        # limpa o terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"🎲 Rolando o dado...\n")
        print(f"[ {numero} ]")

        time.sleep(0.1)

    # resultado final
    resultado = randint(1, lados)

    os.system('cls' if os.name == 'nt' else 'clear')

    print("🎲 Resultado final:")
    print(f"[ {resultado} ]")
    return resultado

class Personagem(ABC):
    def __init__(self,nome,forca,vida, elo,hab_1= 0,hab_2= 0):
        self.nome = nome
        self.forca = forca
        self.vida = vida
        self.elo = elo
        self.hab_1 = hab_1
        self.hab_2 = hab_2

    @staticmethod
    def atacar(dano):
        rolar_d10 = rolar_dados(10)
        if rolar_d10 <= 2:
            return None
        else:
            ataque_efetivo = (rolar_d10 * dano) // 10
            return ataque_efetivo

    def receber_dano(self,dano):
        self.vida -= dano
        return f'{self.nome} recebeu um dano de {dano:.0f} e ficou com {self.vida:.0f}HP'

    def conferir_vida(self):
        if self.vida <= 0:
            return False #MORTO
        else:
            return True #VIVO

    @abstractmethod
    def curar(self):
        pass

# Personagens disponiveis

class Mago(Personagem):
    def __init__(self, nome='Player 1', forca=170, vida=1100, elo=1,hab_1= 0,hab_2= 0):
        super().__init__(nome,forca,vida,elo,hab_1,hab_2)
        self.habilidade = ['Golpe básico']

    def curar(self):
    # Para curar, é jogado um dado d8
        if self.vida == 1100:
            return None
        else:
            cura = 100
            rolar_d8 = rolar_dados(8)
            cura_efetiva = (cura*rolar_d8)/8
            self.vida+= cura_efetiva #adiciona a cura
            self.vida = min(self.vida, 1100)  # Não deixa passar de 1100 de vida
            return cura_efetiva

    def habilidade_1(self, cpu, rodada):
        roubo_vida = self.atacar(self.forca) * 0.2
        cpu.vida -= roubo_vida
        self.hab_1 = rodada + 2 # countdown = 1 rodada
        return (f'{cpu.nome} recebeu 20% do seu ataque em roubo de vida\n'
                f'-{roubo_vida:.0f}HP\n')


class Guerreiro(Personagem):
    def __init__(self,nome='Player 1',forca=200,vida=1000,elo=1,hab_1= 0,hab_2= 0):
        super().__init__(nome,forca,vida,elo,hab_1,hab_2)
        self.habilidade = ['Golpe básico']

    def curar(self):
        # Para curar, é jogado um dado d8
        if self.vida == 1000:
            return None
        else:
            cura = 100
            rolar_d8 = rolar_dados(8)
            cura_efetiva = (cura * rolar_d8) / 8
            self.vida += cura_efetiva #adiciona a cura
            self.vida = min(self.vida, 1000) # Não deixa passar de 1000 de vida
            return cura_efetiva

class Arqueiro(Personagem):
    def __init__(self,nome='Player 1',forca=230,vida=900,elo=1,hab_1= 0,hab_2= 0):
        super().__init__(nome,forca,vida,elo,hab_1,hab_2)
        self.habilidade = ['Golpe básico']

    def curar(self):
        # Para curar, é jogado um dado d8
        if self.vida == 900:
            return None
        else:
            cura = 100
            rolar_d8 = rolar_dados(8)
            cura_efetiva = (cura * rolar_d8) / 8
            self.vida += cura_efetiva  # adiciona a cura
            self.vida = min(self.vida, 900)  # Não deixa passar de 900 de vida
            return cura_efetiva

# INIMIGOS

class BestaCauda(Personagem):
    def __init__(self,nome='Besta de Cauda',forca=200,vida=1000,elo=1):
        super().__init__(nome,forca,vida,elo)
        # Só tem ataque básico, sem habilidades

    def curar(self):
        # Para curar, é jogado um dado d8
        if self.vida == 1000:
            return None
        else:
            cura = 100
            rolar_d8 = rolar_dados(8)
            cura_efetiva = (cura * rolar_d8) / 8
            self.vida += cura_efetiva  # adiciona a cura
            self.vida = min(self.vida, 1000)  # Não deixa passar de 900 de vida
            return cura_efetiva

class CAO(Personagem):
    def __init__(self,nome='Cão de 3 Cabeças',forca=250,vida=1500,elo=2):
        super().__init__(nome,forca,vida,elo)


    def habilidade(self,p1):
        """
           Diminui 50% do ataque do jogador.
        """
        # diminui 50% o ataque do jogador na proxima jogada
        p1.forca = p1.forca * 0.5
        return (f'{self.nome} utilizou sua habilidade de redução de dano\n'
                f'{p1.nome} perdeu 50% de força de ataque básico e ficou com {p1.forca} atk')

    def curar(self):
        # Para curar, é jogado um dado d8
        if self.vida == 1500:
            return None
        else:
            cura = 100
            rolar_d8 = rolar_dados(8)
            cura_efetiva = (cura * rolar_d8) / 8
            self.vida += cura_efetiva  # adiciona a cura
            self.vida = min(self.vida, 1500)  # Não deixa passar de 900 de vida
            return cura_efetiva


class Capirava(Personagem):
    def __init__(self,nome='Cão de 3 Cabeças',forca=350,vida=2500,elo=2,hab_1 = 500):
        super().__init__(nome,forca,vida,elo,hab_1)


    def habilidade(self,p1,rodada):
        """
            Bloqueia todas as habilidades por 2 rodadas e ganha 500 atk
        """
        # Bloqueia todas as habilidades do player por 2 rodadas e atacar com 500 atk
        self.atacar(self.hab_1)
        countdown = rodada + 4 # 2 rodadas do player com habilidades bloqueadas
        # 3 rodadas do CPU para usar novamente a habilidade
        return countdown

    def curar(self):
        # Para curar, é jogado um dado d8
        if self.vida == 1500:
            return None
        else:
            cura = 100
            rolar_d8 = rolar_dados(8)
            cura_efetiva = (cura * rolar_d8) / 8
            self.vida += cura_efetiva  # adiciona a cura
            self.vida = min(self.vida, 1500)  # Não deixa passar de 900 de vida
            return cura_efetiva