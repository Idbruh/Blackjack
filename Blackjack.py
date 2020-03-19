import random

class Blackjack:
    def __init__(self,carta=None):
        self.baralho = [{'A':11},{'A':1},{'2':2}, {'3':3}, {'4':4}, {'5':5}, {'6':6}, {'7':7}, {'8':8}, {'9':9},
                        {'10':10},{'J':10},{'Q':10},{'K':10}]
        self.mao_jogador = []
        self.carta = carta
        self.carta_especial = [ {'Q':10},{'K':10}]
        self.carta_int = [{'A':1},{'2':2}, {'3':3}, {'4':4}, {'5':5}, {'6':6}, {'7':7}, {'8':8}, {'9':9},{'10':10}]

        self.nome_jogador = ''


    def escolhe_carta(self):
        self.carta = random.choice(self.baralho)
        self.mao_jogador.append(self.carta)
        return self.carta
    def numero_de_rodadas(self):
        pass

    def check_as(self):
        if self.mao_jogador == 0:
            self.carta = [{'A': 11}]
            self.mao_jogador.append(self.carta)
            return self.mao_jogador
        if self.mao_jogador in self.carta_int:
            self.carta = [{'A': 1}]
            return self.mao_jogador.append(self.carta)

    def valida_vencedor(self):
        if sum(self.mao_jogador) == 21:
            return print(f'{self.nome_jogador} Você ganhou!!')
        if sum(self.mao_jogador) < 21:
            return print(f'{self.nome_jogador} A sua pontuação é {self.mao_jogador}!!')
        if sum(self.mao_jogador) > 21:
            return print(f'{self.nome_jogador} Voce perdeu!!')

    def jogador(self):

        pass
    def menu(self):
        self.a = print(int(input('''
            |Blackjack
            |    REGRAS BÁSICAS:
 
                    ° Jogador começa com um carta (dada pelo computador, modo randômico);
                    ° Perguntar para o jogador se ele quer continuar jogando ou parar;
                    ° Se o jogador escolher parar, mostrar a pontuação geral;
                    ° Se o jogador escolher continuar, enviar mais uma carta;
                    ° A carta ÁS , na primeira vez que é tirada, vale 11. Se a segunda carta for uma LETRA, o ÁS continua
                      valendo 11. Porém, se a segunda carta for um NÚMERO, o ÁS passa a valer 1.
                   
        ''')))
        if self.a == 1:
            return print('numero 1')
        if self.a == 2:
            return print('numero 2')

    def dashboard(self):











b= Blackjack()
print(b.menu())