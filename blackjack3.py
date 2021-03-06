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
        self.dealer_hand = []
        self.player_hand = []

    def comecar_jogo(self):
        self.opc = self.game_menu()
        self.n_player = self.num_player()
        self.deck = self.deck()
        self.define_all_players()
        self.rodadas()

    def game_menu(self):
        self.opc = print('''
═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ .
                                 _     _            _    _            _    
                                | |   | |          | |  (_)          | |   
                                | |__ | | __ _  ___| | ___  __ _  ___| | __
                                | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
                                | |_) | | (_| | (__|   <| | (_| | (__|   <   _
                                |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ (_)
                                                       _/ |                
                                                      |__/   
                                    ______
                            ______ |J  ww|
                            |A .  || /\{)| 
                            | /.\ || \/% | 
                            |(_._)||   % | 
                            |  |  ||__%%[|
                            |____V|  

»» Rules:
» You're betting against the Dealer. 
» Both of you enters the game with 1 card in hand ad you'll be seeing each others hand, so you are able to decide if:
    Hit: Take another card from the dealer.
    Stand: Take no more cards.
» Wins the one who gets closer or equal to 21 points...
                                                        Good Luck!

♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ . ♠ ♡ ♢ ♣ .
═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════        ''')

    def deck(self):
        self.deck = []
        for valores in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'Ten', 'Q', 'J', 'K']:
            for naipe in [' of Spade ♠ ', ' of Heart ♡ ', ' of Diamond ♢ ', ' of Club ♣ ']:
                self.deck.append(str(valores) + naipe)
        shuffle(self.deck)
        return self.deck

    def num_player(self):
        n_player = int(input('\nInform the number of players.  1-6\n» '))
        while n_player > 6:
            print("The total number of players cannot be higher than 6. You must have a dealer in this game!\n")
            n_player = int(input('Inform the number of players.  1-6\n\n» '))
        print(f"The numbers of players is {n_player + 1}. And you'll be playing along with the Dealer")
        return n_player

    def cria_players_hand_individualy(self):
        individual_player = [{'Player': self.p_name}, {'Score': self.conta_pontos(self.player_cards)},
                             {'Your hand is': self.player_cards}]
        return individual_player

    def player_name(self):
        self.p_name = input(f"Inform the player's name\n» ")
        self.player_cards.append(self.deck.pop())
        self.individual_player = self.cria_players_hand_individualy()
        self.all_players.append(self.individual_player)

    def rodadas(self):
        jogador_atual = 0
        conta_rodadas = 0
        self.dealer_hand.append(self.deck.pop())
        while self.conta_pontos(self.dealer_hand) <= 17 and conta_rodadas < 5:
            self.dealer_hand.append(self.deck.pop())
            conta_rodadas += 1
        conta_rodadas = 0
        print(f"Dealer's hand\n{self.dealer_hand}")
        for player in self.all_players:
            while conta_rodadas < 5:
                opcao = input(f'''
═══════════════════════════════════════════════════════
                                                       
» {player[0]['Player']}, your total Score is: {self.conta_pontos(player[2]['Your hand is'])}                           
» Your hand is: {player[2]['Your hand is']}             
                                                       
═══════════════════════════════════════════════════════
»» Would you like to go for a Hit? 1. Yes | 2. No     
»  ''')
                if opcao == '1' or opcao.lower == 'yes':
                    self.all_players[jogador_atual][2]['Your hand is'].append(self.deck.pop())
                else:

                    if opcao == '2' or opcao.lower == 'no':
                        print(f"{self.p_name}, your choice is to Stand.")
                        break
                conta_rodadas += 1
            self.player_hand = self.all_players[jogador_atual][2]['Your hand is']
            self.player_name = self.all_players[jogador_atual][0]['Player']
            jogador_atual += 1
            self.define_dealer_rulers()

    def define_all_players(self):
        self.dealer_cards = []

        contador = 0
        while contador != self.n_player:
            self.player_cards = []
            self.player_name()
            contador += 1

    def define_dealer_rulers(self):
        pontos_dealer = self.conta_pontos(self.dealer_hand)
        pontos_player = self.conta_pontos(self.player_hand)

        if pontos_dealer > 21:
            print(f'» Player {self.player_name} won. Dealer busted!\n\n Congrats, {self.player_name}.  ☺ ')
        elif pontos_player > 21:
            print(f'» Dealer won. Player {self.player_name} busted!')
        elif pontos_dealer == pontos_player:
            print(f'» Player {self.player_name}, you and the Dealer ended up the game as Even!')
        elif pontos_dealer > pontos_player or pontos_dealer == 21:
            print(f'» Dealer won {self.player_name} with {str(pontos_dealer)} points!')
        elif pontos_dealer < pontos_player or pontos_player == 21:
            print(f'» {self.player_name} won with {str(pontos_player)} points!')

    def conta_pontos(self, mao):
        pontos = 0
        for card in mao:
            if card[0] == 'J' or card[0] == 'Q' or card[0] == 'K' or card[0] == 'T':
                pontos += 10
            elif card[0] != 'A':
                pontos += int(card[0])
            elif card[0] == 'A' and pontos >= 10:
                pontos += 1
            else:
                pontos += 11

        return pontos


b = Blackjack()
b.comecar_jogo()
