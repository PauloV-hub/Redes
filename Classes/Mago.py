# Lvl.5 Wizard Bladesinger Turtle
# Combate:
# Bladesong ativado durante o combate(soma Inteligência na CA), armadura arcana já ativada também

# Stats:
# STR: 8 | DEX: 18 | CON: 16 | INT:16 | WIS:8 | CHA:8
import math
import random
from colorama import init, Fore, Style, Back

init(autoreset=True)

bonusProficiencia = 3


class Mago:

    espacos1Ciclo = 4
    espacos2Ciclo = 3
    espacos3Ciclo = 2
    

    dodgeAction = False

    def __init__(self):
        self.CA = 20  # CA = 13(armadura arcana) + 4(destreza) + 3(bladesong)
        self.HP = 37
        self.salvaguarda = 15
        self.strength = -1
        self.destreza = 4
        self.wisdom = -1
        self.charisma = -1
        self.constituicao = 3
        self.inteligencia = 3
    def critico(self,d20, dano):
        if(d20==20):
            return dano*2
        else:
            return dano
    def print(self,d20Final,dano):
         print(
            Back.MAGENTA
            + Fore.WHITE
            + Style.BRIGHT
            + "Seu d20: "
            + str(d20Final)
            + "\nSeu dano: "
            + str(dano)
        )
    

    def ataqueAcerto(self):
        ataqueValido = False
        while(ataqueValido == False):
            acao = input(
                Back.MAGENTA
                + Fore.WHITE
                + Style.BRIGHT
                + "Qual ação deseja fazer?\n(1)Lâmina das trevas + Lâmina estrondosa (2) Bola de fogo\n "
            )
            dano = 0
            if (acao == "1"):
                d20 = random.randint(1, 20)
                d20Final = d20 + self.destreza + bonusProficiencia
                for i in range(1, 4):
                    d8 = random.randint(1, 8)
                    dano = dano + d8
                dano = dano + self.destreza
                dano = self.critico(d20Final,dano)
                self.print(d20Final, dano)
                msg = "D" + "AT" + str(d20Final).zfill(2) + str(dano)
                ataqueValido = True
                return msg
            elif(acao == "2" and self.espacos3Ciclo > 0):
                self.espacos3Ciclo = self.espacos3Ciclo - 1
                d20Final = self.salvaguarda
                for i in range(1, 8):
                    d6 = random.randint(1, 6)
                    dano = dano + d6
                self.print(d20Final, dano)
                msg = "D" + "ED" + str(self.salvaguarda).zfill(2) + str(dano)
                ataqueValido = True
                return msg
            else:
                print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT + "Digite uma Ação Válida! \n Você não possui o espaço de magia necessário!!")
                ataqueValido = False
                
    def getTeste(self,atributo, msg):
        d20 = random.randint(1,20)
        salvaguarda = d20 + atributo
        if(int(msg[2:4]) > salvaguarda):
            dano = math.ceil(int(msg[4:6]))
        else:
            dano = math.ceil(int(msg[4:6])/2)
        return dano

    def ataqueRecebido(self, msg):

        if (msg[:2] == "ES") :
                dano = self.getTeste(self.strength,msg)
        elif(msg[:2] =="ED" ):
                dano = self.getTeste(self.destreza,msg)
        elif(msg[:2] =="EI" ):
                dano = self.getTeste(self.inteligencia,msg)
        elif(msg[:2] =="EW" ):
                dano = self.getTeste(self.wisdom,msg)
        elif(msg[:2] =="EC" ):
                dano = self.getTeste(self.constituicao,msg)
        elif(msg[:2] =="EH"):
                dano = self.getTeste(self.charisma,msg)
        elif msg[:2] == "AT" and int(msg[2:4]) >= self.CA:
            # Se o ataque for menor que CA+5, usa shield
            if int(msg[2:4]) < (self.CA + 5) and self.espacos1Ciclo > 0:
                self.espacos1Ciclo = self.espacos1Ciclo - 1
                print(
                    Back.MAGENTA
                    + Fore.WHITE
                    + Style.BRIGHT
                    + "Você usou Escudo Arcano! Seu inimigo errou o Ataque, seu d20 foi: "
                    + msg[1:3]
                )
                if self.espacos1Ciclo == 3:
                    print(
                        Back.MAGENTA
                        + Fore.WHITE
                        + Style.BRIGHT
                        + "\nEspaços de magia restantes:\n1º Ciclo: [x][][][]"
                    )
                if self.espacos1Ciclo == 2:
                    print(
                        Back.MAGENTA
                        + Fore.WHITE
                        + Style.BRIGHT
                        + "\nEspaços de magia restantes:\n1º Ciclo: [x][x][][]"
                    )
                if self.espacos1Ciclo == 1:
                    print(
                        Back.MAGENTA
                        + Fore.WHITE
                        + Style.BRIGHT
                        + "\nEspaços de magia restantes:\n1º Ciclo: [x][x][x][]"
                    )
                if self.espacos1Ciclo == 0:
                    print(
                        Back.MAGENTA
                        + Fore.WHITE
                        + Style.BRIGHT
                        + "\nEspaços de magia restantes:\n1º Ciclo: [x][x][x][x]"
                    )
                dano = 0
            else:
                dano = int(msg[4:6])
        else:
            print(
                Back.MAGENTA
                + Fore.WHITE
                + Style.BRIGHT
                + "Seu inimigo errou o Ataque, seu d20 foi: "
                + msg[2:4]
            )
            dano = 0

        print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT + "Dano recebido : " + str(dano))

        nova_vida = self.HP - dano
        self.HP = nova_vida
        return nova_vida
