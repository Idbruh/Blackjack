# fazer um metodo para criar o baralho - ok
# criar um metodo que define o numero de rodadas - ok
# criar um metodo que define a quantidade de jogadores - ok
# criar um metodo que salva o baralho tanto do dealer qt do jogador
# criar um metodo para verificar o ace
# criar um metodo para verificar quem ganhou
# criar metodo de regras do dealer
from random import shuffle


class Blackjack:

    def __init__(self):
        self.player_cards = []
        self.n_player = 0
        self.dealer = None
        self.game = ''
        self.new_card = None
        self.contador = 0
        self.pontos = 0
        self.all_players = []
        self.hand_dealer = []
        self.dealer_hand = []

    # the game runs
    def comecar_jogo(self):
        self.n_player = self.num_player()
        self.deck = self.deck()
        self.define_all_players()
        for player in self.all_players:
            print(player)

    # metodo that creates and shuffles the deck
    def deck(self):
        self.deck = []
        for valores in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'Ten', 'Q', 'J', 'K']:
            for naipe in [' of Spade ♠ ', ' of Heart ♡ ', ' of Diamond ♢ ', ' of Club ♣ ']:
                self.deck.append(str(valores) + naipe)
        shuffle(self.deck)
        return self.deck

    # criar um metodo que define a quantidade de jogadores
    def num_player(self):
        n_player = int(input('Inform the number of players.  1-6\n\n --->'))
        print(f"The numbers of players is {n_player + 1}. And you'll be playing along with the Dealer")
        return n_player

    # cria um jogador individual
    def cria_players_hand_individualy(self):
        individual_player = [{'Player:': self.p_name}, {'Score:': self.conta_pontos()},
                             {'Your hand is so far:': self.player_cards}]
        return individual_player

    # definindo nome dos jogadores
    def player_name(self):
        self.p_name = input(f"Inform the player's name: ")
        self.player_cards.append(self.deck.pop())
        self.player_cards.append(self.deck.pop())
        self.individual_player = self.cria_players_hand_individualy()
        self.all_players.append(self.individual_player)

    # definir mão do player e do dealer
    def hand_setup(self):
        self.dealer_hand = []
        self.player_hand = []

    # definir todos os jogadores

    def define_all_players(self):
        self.dealer_cards = []

        contador = 0
        while contador != self.n_player:
            self.player_cards = []
            self.player_name()
            contador += 1

    # defin regra do dealer
    def define_dealer_rulers(self):
        self.hand_setup()
        pontos_dealer = self.conta_pontos(self.hand_dealer)
        pontos_player = self.conta_pontos(self.player_hand)
        if pontos_dealer == pontos_player:
            print(f'Player {self.player_name}, you and the Dealer ended up the game as Even!')
        if self.pontos_dealer > pontos_player:
            print(f'Dealer won, {self.player_name} with {str(pontos_dealer)} points!')
        if self.pontos_dealer < pontos_player:
            print(f' {self.player_name} won with {str(pontos_player)} points!')
            # minha lógica e esforços terminaram aqui, por hoje....

    # definir um metodo que conta os pontos e já aplica as regras do Ás

    def conta_pontos(self):
        self.conta_carta = 0
        for cards in self.player_cards:
            if cards[0] == 'J' or cards[0] == 'Q' or cards[0] == 'K' or cards[0] == 'T':
                self.conta_carta += 10
            elif cards[0] != 'A':
                self.conta_carta += int(cards[0])
            elif cards[0] == 'A' and self.conta_carta >= 10:
                self.conta_carta += 1
            else:
                self.conta_carta += 11

        return self.conta_carta


b = Blackjack()
b.comecar_jogo()
