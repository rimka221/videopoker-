import pandas as pd
import random
class VideoPoker:
    def __init__(self):
        self.deck = []
    def init_deck(self):
        self.deck =  ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']
        return self.deck
    def premier_tirage(self,deck):
        tirage = random.sample(deck, 5)
        for item in deck:
            deck.remove(item)
        return tirage, deck

    def choix_carte(self,tirage):
        remove_card = []
        for item in tirage:
            print('gardez cette carte y/n : ', item)
            bol = input()
            if (bol == 'n'):
                remove_card.append(item)
        for item in remove_card:
            tirage.remove(item)
        return tirage
    def deuxieme_tirage(self,jeu):
        if (len(jeu) < 5):
            remaining = random.sample(self.deck, 5 - len(jeu))
            for item in remaining:
                jeu.append(item)
        return jeu
    def machine(self):
        my_tuple = self.premier_tirage(self.deck)
        first = my_tuple[0]
        print("Le premier tirage {}".format(first))
        choice = self.choix_carte(first)
        jeu = self.deuxieme_tirage(choice)
        print(jeu)
        return jeu
    def is_consecutive(self,jeu):
        return sorted(jeu) == list(range(min(jeu), max(jeu) + 1))
    def is_win(self,jeu):
        multiply = 0
        card_list = []
        color_list = []
        royal = [10, 11, 12, 13, 14]
        result = " Vous avez perdu "
        for item in jeu:
            card, color = item.split('-')
            card_list.append(card)
            color_list.append(color)
            duplicates_color = pd.Series(color_list).value_counts()
        for i in range(0, len(card_list)):
            if card_list[i] == 'J':
                card_list[i] = 11
            if card_list[i] == 'Q':
                card_list[i] = 12
            if card_list[i] == 'K':
                card_list[i] = 13
            if (card_list[i] == 'A'):
                card_list[i] = 14
            card_list[i] = int(card_list[i])
        for item in card_list:
            my_count = card_list.count(item)
            if my_count == 2:  # paire or double paire
                multiply += 1
                result = "Bravo un paire ou double paire "
            if my_count == 3:  # brelan
                multiply = 6
                result = "Bravo un Brelan"
                if multiply == 1:  # full
                    multiply = 9
            if my_count == 4:
                multiply = 25
                result = "Bravo un FULL"
            if max(duplicates_color == 5):  # Flush
                multiply = 6
                result = "Bravo un FLUSH"
            print(card_list)
            if self.is_consecutive(card_list):  # quinte
                multiply = 4
                result = "Bravo un Quinte"
                if max(duplicates_color == 5):  # Quinte Flush
                    multiply = 50
                    result = "Bravo un Quinte Flush"
                    if sorted(royal) == sorted(card_list):
                        multiply = 250          #Royal Quinte Flush
                        result = "Bravo un Quinte Flush Royal awesome"
        return multiply, result

    def calcul_gain(self, jeu, mise):
        multiply, result = self.is_win(jeu)
        return multiply * mise, result

    def partie(self, bankrool, mise):
        jeu = self.machine()
        bankrool -= mise
        gain, result = self.calcul_gain(jeu, mise)
        bankrool += gain
        return bankrool, result

    def video_poker(self):
        self.init_deck()
        print("**************Bienvenue dans votre jeu video poker**************")
        print("* Inserer votre bankroll                                       *")
        bankroll = int(input())
        response = True
        while response:
            print("* Saississez votre mise                                        *")
            mise = int(input())
            bankroll, result = self.partie(bankroll, mise)
            print(result)
            print("Votre solde actuel {} € ".format(bankroll))
            print("Voulez-vous continuer y/n")
            bol = input()
            if bol == 'n':
                response = False
        print('Bye à la prochaine')
