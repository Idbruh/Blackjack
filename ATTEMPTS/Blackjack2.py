from random import shuffle

class Blackjack:


    def __init__(self):
        self.player_cards = None
        self.n_player = 0
        self.dealer = None
        self.game = ''
        self.new_card = None
        self.conta_ponto()

# metodo that creates and shuffles the deck
    def deck(self):
        self.deck = []
        for valores in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'Ten', 'Q', 'J', 'K']:
            for naipe in [' of Spade ♠ ', ' of Heart ♡ ', ' of Diamond ♢ ', ' of Club ♣ ']:
                self.deck.append(str(valores) + naipe)
        return shuffle(self.deck)

    def num_player(self):
        self.n_player = int(input('Inform the number of players.  1-6\n\n --->'))
        return print(f"The numbers of players is {self.n_player + 1}. And you'll be playing along with the Dealer")


    def conta_player(self):
        self.contador = 0
        self.p_list = []
        self.p_name = input(f"Inform the player's name: ")
        while self.contador < self.n_player:
            self.p_list.append(self.p_name + f'{self.pontos}: ')
            self.contador += 1
        return self.contador

    def start_game(self):
        self.deck = self.deck()

        for player in range(len(self.p_list)):
            self.option = input(f'Gostaria de outra carta, {self.p_name}?  y / n\n\n')
        if self.option.lower() == 'y':
            for self.carta in self.deck:
                self.new_card = self.deck

    def cria_players_hand_individualy(self):
        self.individual_player = [{'Player:': self.p_name }, {'Score:'}]
        return self.individual_player



# regra as 21 - 10
        if self.conta_carta > 21:
            for card in self.player_cards:
                if card[0] == 'A':
                    self.conta_carta -= 10
                    if self.conta_carta <= 21:
                        return self.conta_carta




    # def embaralhar(self):
    #     for i in range(len(self.nome_jogador)):
    #         virar_carta = input('deseja virar carta? (1-Yes / 0-No):')
    #         try:
    #
    #             while (virar_carta == '1'):
    #                 escolha = random.choice(self.valores_cartas)
    #                 self.nome_jogador[i]['total pontos'] = self.nome_jogador[i]['total pontos'] + escolha["valor"]
    #                 print(self.nome_jogador[i]['total pontos'])
    #                 virar_carta = input(
    #                     'Jogador ' + self.nome_jogador[i]['nome'] + ' deseja virar carta? (1-Yes / 0-No):')


    def player(self):
        self.nome = input('')



    def conta_ponto(self):
        self.conta_carta = 0
        self.ace_count = 0
        for cards in self.player_hand:
            if int(cards[0]) == 'J' or int(cards[0])  == 'Q' or int(cards[0])  == 'K' or int(cards[0]) == 'T':
                self.conta_carta += 10
            elif cards[1] != 'A':
                self.conta_carta += int(cards[0])
            else:
                self.ace_count += 1
            if self.ace_count == 1 and self.conta_carta >= 10:
                self.conta_carta += 1
            else:
                self.ace_count += 1 and self.conta_carta

            if self.ace_count == 1 and self.conta_carta >= 10:
                self.conta_carta += 11
            else:
                self.conta_carta += 1
            return self.conta_carta

    def save_player_hand(self):
        for player in range(len(self.p_list)):
            pass


    def hand_setup(self):
        self.dealer_hand = []
        self.player_hand = []


        # while self.conta_pontos(self.dealer_hand) <= 16:
        #     self.dealer_hand.append(self.deck().pop())
        # return self.dealer_hand, self.player_hand  # aumenta a mão do dealer ate chegar 16 pontos

    # retorna


    def playerhand(self):
        self.hand_setup()
        self.conta_ponto()
        #while self.conta_ponto(self.player_hand):

    # def init_turn(self):
    #     self.cont = 0
    #     self.dealer_hand.append(self.deck.pop())
    #     self.dealer_hand.append(self.deck.pop())
    #     for card in range(len(self.p_list)):
    #         self.total_p_cards =





    def turns(self):
        self.rodadas = 0
        while self.rodadas != 5:
            for card in range(len(self.p_list)):
                self.rodadas += 1
                self.dealer_hand.append(self.deck.pop())
                self.player_hand.append(self.deck.pop())
            break

        while self.game != 'exit':
            self.dealer_pontos = self.conta_pontos


# player = int(input('Quantos jogadores?   1-6'))
#
# for jogadores in player:
#     pass

bj = Blackjack()
print(bj.deck())










#rodadas

#while != 5:



a = Blackjack()
print(a.deck)

