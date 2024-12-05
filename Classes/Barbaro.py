import random
import math
from colorama import init, Fore, Style, Back
# STR: 18 | DEX: 16| CON: 16 | INT: 8 | WIS: 8 | CHA: 8
init(autoreset=True)


class Barbaro:

    def __init__(self):
        self.CA = 15
        self.HP = 55
        self.strength = 4
        self.destreza = 3
        self.wisdom = -1
        self.charisma = -1
        self.constituicao = 3
        self.inteligencia = -1
        self.trunfoFinal = False
        self.esquivo = False
        self.danoFuria = 3
        self.Imprudente = False
        self.orc = False

    def ataqueAcerto(self):
        auxiliar = 0
        dano = 0
        d20 = 0
        imprudente = input(
            Back.RED
            + Style.BRIGHT
            + "Deseja usar ataque imprudente?\n (1) Sim \n (2) Não\n "
        )
        if imprudente == "1":
            self.Imprudente = True
        else:
            self.Imprudente = False
        ataque = input(
            Back.RED
            + Style.BRIGHT
            + "Deseja usar ataque utilizar?\n (1) Ataque com Machado 2x (2) Modo ESQUIVO\n "
        )
        if ataque == "1":
            d12 = random.randint(1, 12)
            dano = (2*d12) + 5 + self.danoFuria
            d20 = random.randint(1, 20)   # Dado d20
            d20Final = d20 + 3 + 5  # d20 + Bonus de proeficiencia + strength
            if self.Imprudente == True:
                auxiliar = d20Final + 5
            print(
                Style.BRIGHT
                + Back.RED
                + "Seu d20: "
                + str(auxiliar)
                + "\nSeu dano: "
                + str(dano)
            )
        else:
            self.esquivo = True
            auxiliar = 0
            dano = 0
            print(
                Style.BRIGHT
                + Back.RED
                + "Modo Esquivo ativado! Me acerta que eu duvido"
            )
        dano = self.critico(d20,dano)
        msg = "D" + "AT" + str(auxiliar).zfill(2) + str(dano)
        return msg
        # A mensagem de ataque agora inclui o valor correto do dano
    def critico(self,d20, dano):
        if(d20==20):
            return 2*dano
        else:
            return dano
    def getTeste(self,atributo, msg):
        d20 = random.randint(1,20)
        salvaguarda = d20 + atributo
        if(int(msg[2:4]) > salvaguarda):
            dano = math.ceil(int(msg[4:6]))
        else:
            dano = math.ceil(int(msg[4:6])/2)
        return dano
    def ataqueRecebido(self, msg):
        if self.esquivo == True:
            CA = self.CA + 5
        elif self.Imprudente == True:
            CA = self.CA - 2
        else:
            CA = self.CA
        if (msg[:2] == "ES") :
                dano = (self.getTeste(self.strength,msg))/2
        elif(msg[:2] =="ED" ):
                dano = (self.getTeste(self.destreza,msg))/2
        elif(msg[:2] =="EI" ):
                dano = (self.getTeste(self.inteligencia,msg))/2
        elif(msg[:2] =="EW" ):
                dano = (self.getTeste(self.wisdom,msg))/2
        elif(msg[:2] =="EC" ):
                dano = (self.getTeste(self.constituicao,msg))/2
        elif(msg[:2] =="EH"):
                dano = (self.getTeste(self.charisma,msg))/2
        elif msg[:2] == "AT" and int(msg[2:4]) >= CA:
            dano = math.ceil(int(msg[4:6]) / 2)
        else:
            print(
                Style.BRIGHT
                + Back.RED
                + "Seu inimigo errou o Ataque, seu d20 foi: "
                + msg[2:4]
            )
            dano = 0
        print(Style.BRIGHT + Back.RED + "Dano recebido : " + str(dano))

        nova_vida = self.HP - dano
        if (dano > 10 and self.trunfoFinal == False):
            Irina = input(
                Style.BRIGHT
                + Back.RED
                + "Você irá sofrer um dano monstruoso\n Deseja utilizar seu Trunfo Final(única utilização)? \n (1)Sim \n (2) Não\n "
            )
            if Irina == '1' :
                print(
                Style.BRIGHT
                + Back.RED
                + "Sunny lhe salvou, Parabéns Effie, parece que você tem bons amigos ao seu lado!!!"
                )
                self.trunfoFinal = True
                nova_vida += 20    
        
        if nova_vida <= 0 and self.orc == False:
            nova_vida = 1
            self.orc = True
            print(Style.BRIGHT + Back.RED + "EU SOU ORC !!!\n")

        self.HP = nova_vida
        self.Imprudente = False
        self.esquivo = False
        return nova_vida


