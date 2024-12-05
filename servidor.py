import random
import socket
import sys
from Classes.Barbaro import Barbaro
from Classes.Clerigo import Clerigo
from Classes.Ladino import Ladino
from Classes.Mago import Mago
from colorama import init, Fore, Back, Style

init(autoreset=True)

bonusProficiencia = 3


class Personagem:
    def __init__(self, classe):
        self.nome = None
        self.classe = None

        # Definindo a classe com base no parâmetro recebido
        if classe == "1":
            self.nome = "Groak"
            print(
                Fore.YELLOW
                + "\nVocê escolheu um Bárbaro!\nParabéns por escolher o Herói Groak!\n"
            )
            self.classe = Barbaro()
        elif classe == "2":
            self.nome = "Oliver"
            print(
                Back.MAGENTA
                + Fore.WHITE
                + Style.BRIGHT
                + "\nVocê escolheu um Mago!\nParabéns por escolher o herói Oliver!\n"
            )
            self.classe = Mago()
        elif classe == "3":
            self.nome = "Nephis"
            print(
                Fore.YELLOW
                + "\nVocê escolheu um Clérigo!\nParabéns por escolher Nephis, Estrela da mudança\n"
            )
            self.classe = Clerigo()
        elif classe == "4":
            self.nome = "Sarah"
            print(
                Fore.YELLOW
                + "\nVocê escolheu um Ladino!\nParabéns por escolher Sarah Frostriver!\n"
            )
            self.classe = Ladino()


def main():

    socketConexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    endereco = ("127.0.0.1", 50000)
    socketConexao.bind(endereco)
    socketConexao.listen(1)

    [jogador, _] = socketConexao.accept()

    personagem1 = Personagem(
        input(
            Fore.YELLOW
            + "Escolha a classe do Personagem 1:\n(1)Barbaro\n(2)Mago\n(3)Clerigo\n(4)Ladino\n "
        )
    )

    encerrado = False

    while not encerrado:
        print(Fore.CYAN + "Sua vez\n")
        msg = personagem1.classe.ataqueAcerto()  # Atacando o Inimigo,

        jogador.send(
            msg.encode()
        )  # enviar teste ou D20 e o dano, msg = D +'AD' + '18' + '30'

        retorno = jogador.recv(1)  # mensagem

        if not retorno:
            sys.exit(-1)
        retorno = retorno.decode()

        if retorno == "D":
            acaoInimigo = jogador.recv(6)  # teste ou D20 e o Dano
            acaoInimigo = acaoInimigo.decode()
            hpRestante = personagem1.classe.ataqueRecebido(acaoInimigo)
            print(Fore.CYAN + "\nSeu HP restante é: " + str(hpRestante))
            if hpRestante <= 0:
                jogador.send("V".encode())
                encerrado = True
                break
            # msg = 'AD' + '18' + '30'
        elif retorno == "V":
            print(Fore.YELLOW + f"\n👑 {personagem1.nome} Ganhou!👑\n")
            encerrado = True
            break


if __name__ == "__main__":
    main()
