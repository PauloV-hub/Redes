import random
import math
from colorama import init, Fore, Style, Back

init(autoreset=True)


class Clerigo:

    espacos1Ciclo = 4
    espacos2Ciclo = 3
    espacos3Ciclo = 2

    def __init__(self):
        self.CA = 16
        self.HP = 43
        self.strength = 8
        self.destreza = 16
        self.wisdom = 14
        self.charisma = 10
        self.constituicao = 16
        self.inteligencia = 8
        self.esquivo = False
        self.danobase = 3
        self.CHAMA = False
        self.arma = False
        self.corpo = False
        self.armadura = False
        self.cura = False
        self.modificadorSabedoria = 4

    def ataqueAcerto(self):
        auxiliar = 0
        dano = 0
        # arma -> mais dano menos ca
        # armadura -> mais ca menos dano
        # corpo -> mais ca e dano
        escolha = input(
            Back.YELLOW
            + Style.BRIGHT
            + "Deseja usar habilidade de aspecto na arma, corpo ou armadura radiante?\n (1) arma \n (2) corpo\n (3) armadura\n "
        )
        if escolha == "1":
            self.arma = True
        elif escolha == "2":
            self.corpo = True
        else:
            self.armadura = True

        ataque = input(
            Back.YELLOW
            + Style.BRIGHT
            + "Deseja usar ataque utilizar?\n(1) Ataque certeiro\n(2) Estilo de batalha fluído\n(3) Chama imortal\n "
        )

        if ataque == "1":
            d12 = random.randint(1, 12)
            dano = d12 + self.danobase - 2
            auxiliar = random.randint(1, 20) + 10

            if self.armadura == True:
                auxiliar -= 2
            if self.corpo == True:
                auxiliar += 3
            if self.arma == True:
                auxiliar += 6
            print(
                Back.YELLOW
                + Style.BRIGHT
                + "Seu d20: "
                + str(auxiliar)
                + "\nSeu dano: "
                + str(dano)
            )

        if ataque == "2":
            d12 = random.randint(1, 12)
            dano = d12 + self.danobase + 5
            auxiliar = random.randint(1, 20)
            self.esquivo = True

            if self.armadura == True:
                auxiliar -= 2
            if self.corpo == True:
                auxiliar += 3
            if self.arma == True:
                auxiliar += 6
            print(
                Back.YELLOW
                + Style.BRIGHT
                + "Seu d20: "
                + str(auxiliar)
                + "\nSeu dano: "
                + str(dano)
            )

        if ataque == "3":
            self.esquivo = True
            self.armadura = True
            self.cura = True
            auxiliar = 0
            dano = 0
            print(Back.YELLOW + Style.BRIGHT + "hack ativado")

        msg = "D" + "AT" + str(auxiliar).zfill(2) + str(dano)
        return msg
        # A mensagem de ataque agora inclui o valor correto do dano

    def ataqueRecebido(self, msg):
        if self.armadura == True:
            CA = self.CA + 5
        if self.esquivo == True:
            CA = self.CA + 5
        if self.corpo == True:
            CA = self.CA + 3
        elif self.arma == True:
            CA = self.CA - 3
        else:
            CA = self.CA
        if msg[:1] == "E" :
            if(msg[1:2] =="S" and int(msg[2:4]) > self.strength):
                dano = math.ceil(int(msg[4:6]))
            elif(msg[1:2] =="D" and int(msg[2:4]) > self.destreza):
                dano = math.ceil(int(msg[4:6]))
            elif(msg[1:2] =="I" and int(msg[2:4]) > self.inteligencia):
                dano = math.ceil(int(msg[4:6]))
            elif(msg[1:2] =="W" and int(msg[2:4]) > self.wisdom):
                dano = math.ceil(int(msg[4:6]))
            elif(msg[1:2] =="C" and int(msg[2:4]) > self.constituicao):
                dano = math.ceil(int(msg[4:6]))
            elif(msg[1:2] =="H" and int(msg[2:4]) > self.charisma):
                dano = math.ceil(int(msg[4:6]))
        elif msg[:2] == "AT" and int(msg[2:4]) >= CA:
            dano = int(msg[4:6])
        else:
            print(
                Back.YELLOW
                + Style.BRIGHT
                + "Seu inimigo errou o ataque, seu d20 foi: "
                + msg[2:4],
            )
            dano = 0
        print(Back.YELLOW + Style.BRIGHT + "Dano recebido: " + str(dano))

        nova_vida = self.HP - dano

        if self.cura == True:
            cura_total = 0
            if self.espacos3Ciclo > 0:
                for i in range(1, 6):
                    # Cura com ação Bônus do D&D2024 6d4 + Sabedoria no 3ºciclo
                    d4 = random.randint(1, 4)
                    cura_total += d4
                cura_total += self.modificadorSabedoria
            elif self.espacos2Ciclo > 0:
                for i in range(1, 4):
                    # Cura com ação Bônus do D&D2024 6d4 + Sabedoria no 2ºciclo
                    d4 = random.randint(1, 4)
                    cura_total += d4
                cura_total += self.modificadorSabedoria
            elif self.espacos1Ciclo > 0:
                for i in range(1, 2):
                    # Cura com ação Bônus do D&D2024 6d4 + Sabedoria no 2ºciclo
                    d4 = random.randint(1, 4)
                    cura_total += d4
                cura_total += self.modificadorSabedoria
            else:
                print(
                    Back.YELLOW
                    + Style.BRIGHT
                    + "Você não possui mais espaços de magia restantes!\n"
                )
            print(
                Back.YELLOW
                + Style.BRIGHT
                + "Você curou "
                + str(cura_total)
                + " pontos de vida!\n"
            )
            nova_vida += cura_total

        if nova_vida <= 0 and self.CHAMA == False:
            nova_vida = 10
            self.CHAMA = True

            print(
                Back.YELLOW
                + Style.BRIGHT
                + "\n 🔥 HABILIDADE DE ASPECTO CHAMA IMORTAL 🔥\n"
            )

        self.HP = nova_vida
        self.armadura = False
        self.arma = False
        self.corpo = False
        self.esquico = False
        self.cura = False

        return nova_vida

    