import random
import time
'''
Michael Dao
Goal:Create a Poker Game
'''
deck = ['2(heart)', '3(heart)', '4(heart)', '5(heart)', '6(heart)',
         '7(heart)', '8(heart)', '9(heart)', 'T(heart)', 'J(heart)',
         'Q(heart)', 'K(heart)', 'A(heart)', '2(diamond)', '3(diamond)',
         '4(diamond)', '5(diamond)', '6(diamond)', '7(diamond)', '8(diamond)',
         '9(diamond)', 'T(diamond)', 'J(diamond)', 'Q(diamond)', 'K(diamond)',
         'A(diamond)', '2(spade)', '3(spade)', '4(spade)', '5(spade)', '6(spade)',
         '7(spade)', '8(spade)', '9(spade)', 'T(spade)', 'J(spade)', 'Q(spade)',
         'K(spade)', 'A(spade)', '2(club)', '3(club)', '4(club)', '5(club)', '6(club)',
         '7(club)', '8(club)', '9(club)', 'T(club)', 'J(club)', 'Q(club)', 'K(club)',
         'A(club)']
    

def shuffleDeck(deck):
    random.shuffle(deck)
    
shuffleDeck(deck)


class Player:
    def __init__(self, cards, winCondition):
        self.__cards = cards
        self.__winCondition = winCondition
    def get_cards(self):
        return self.__cards
    def set_cards(self,cards):
        self.__cards = cards
        
    def get_winCondition(self):
        return self.__winCondition
    def dealCards(self, deck):
        self.__cards = [deck.pop(0), deck.pop(0)]
    def printCards(self):
        print(f'Your cards: {self.__cards}')
    def printDealerCards(self):
        print(f"Dealer's cards: {self.__cards}")

class River(Player):
    def __init__(self, cards, winCondition, gameStage):
        super().__init__(cards, winCondition)
        self.__gameStage = gameStage

    def get_gameStage(self):
        return self.__gameStage

    def set_gameStage(self, newStage):
        self._gameStage = newStage

    def addCard(self, deck):
        cards = super().get_cards()
        cards.append(deck.pop(0))

    def dealFlop(self , deck):
        flop = []
        for i in range(3):
            deck.remove(deck[0])
            self.addCard(deck)
            deck.remove(deck[0])
        return flop

    def dealRiver(self, deck):
        deck.pop(0)
        self.addCard(deck)
        deck.pop(0)

    def nextCard(self, deck):
        action = ""
        for i in range(100):
            action = input("Type 'deal' to deal the river.\n")
            if action.lower() == 'deal':
                self.dealRiver(deck)
                self.printCards()
                break
            else:
                print("Please type in 'deal' to continue\n")
                continue
    def printCards(self):
        print(f'River: {super().get_cards()}')

class Game():
    def __init__(self, cards, winCondition, gameState):
        self.dealer = Player(cards, winCondition)
        self.player = Player(cards, winCondition)
        self.currentRiver = River(cards, winCondition, gameState)
    def checkMatches(self):  
        matches = []
        #Checking player 7 cards first
        playerRiver = self.currentRiver.get_cards() + self.player.get_cards()
        print(playerRiver)
        for i in range(len(playerRiver)):
            for j in range(i+1, len(playerRiver)):
                if playerRiver[i][0] == playerRiver[j][0]:
                    print(playerRiver[i][0],playerRiver[j][0])
                    matches.append(playerRiver[i][0])
                    print(matches) 
        return matches
    def _rank(self, c):
        r = c[0]  # '2'..'9','T','J','Q','K','A'
        return {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}[r]

    def _suit(self, c):
        # '2(heart)' -> 'heart'
        i = c.index('(')
        return c[i+1:-1]

    
    def checkPair(self, matches):
        if len(matches) == 1:
            return True
        else:
            return False

    def checkTwoPair(self, matches):
        if len(matches) == 2 and matches[0] != matches[1]:
            return True
        else:
            return False
    def checkTrips(self, matches):
        if len(matches) == 3 and matches[0] == matches[1] and matches[1] == matches[2]:
            return True
        else:
            return False

    def checkQuads(self, matches):
        if len(matches) == 4 and matches[0] == matches[1] and matches[1] == matches[2] and matches[2] == matches[3]:
            return True
        else:
            return False
    def checkFullHouse(self, matches):
        sortedPair = sorted(matches)
        if self.checkTrips(sortedPair[0:3]) == True and len(sortedPair) > 3:
            return True
        
    
    def checkFlush(self):
            playerRiver = self.currentRiver.get_cards() + self.player.get_cards()
            suits = []
            for i in range(len(playerRiver)):
                for j in range(i+1, len(playerRiver)):
                    if playerRiver[i][2] == playerRiver[j][2]:
                        suits.append(playerRiver[i][2])
            if len(suits) >= 10:
                return True
            else:
                return False
    

    def is5Consecutive(self, sorted_ranks):
        if len(sorted_ranks) < 5:
            return False
        for i in range(len(sorted_ranks) - 4):
            a,b,c,d,e = sorted_ranks[i:i+5]
            if a+1==b and b+1==c and c+1==d and d+1==e:
                return True
        return False
    

    def convertToNumber(self, card):
        hierarchy = []
        for i in range(len(card)):
            if card[i][0] == 'A':
                hierarchy.append(1)
                hierarchy.append(14)
            elif card[i][0] == 'T':
                hierarchy.append(10)
            elif card[i][0] == 'J':
                hierarchy.append(11)
            elif card[i][0] == 'Q':
                hierarchy.append(12)
            elif card[i][0] == 'K':
                hierarchy.append(13)
            else:
                value = int(card[i][0])
                hierarchy.append(value)
        return sorted(hierarchy)


    def checkStraight(self):
        #Combining player and river cards
        playerRiver = self.currentRiver.get_cards() + self.player.get_cards()
        hiearchy = self.convertToNumber(playerRiver) #Converting cards to numbers
     
        print(playerRiver)
        hiearchy = sorted(hiearchy)
        #Checking for 5 consecutive numbers
        print(hiearchy)
        for i in range(3):
            ls = hiearchy[i], hiearchy[i+1], hiearchy[i+2], hiearchy[i+3], hiearchy[i+4]
            if self.is5Consecutive(ls) == True:
                return True
        return False
    
    def checkStraightFlush(self):
        cards = self.currentRiver.get_cards() + self.player.get_cards()

        # group unique ranks by suit
        by_suit = {'heart': set(), 'diamond': set(), 'spade': set(), 'club': set()}
        for c in cards:
            by_suit[self._suit(c)].add(self._rank(c))

        # check straight inside each suit with >=5 cards
        for suit, ranks in by_suit.items():
            if len(ranks) < 5:
                continue
            uniq = sorted(ranks)
            # Ace low handling (A-2-3-4-5)
            if 14 in uniq:
                uniq = sorted(set(uniq) | {1})
            if self.is5Consecutive(uniq):
                return True
        return False
    
    def checkRoyalFlush(self):
         cards = self.currentRiver.get_cards() + self.player.get_cards()

        # group unique ranks by suit
         by_suit = {'heart': set(), 'diamond': set(), 'spade': set(), 'club': set()}
         for c in cards:
            by_suit[self._suit(c)].add(self._rank(c))

         royal = {10,11,12,13,14}

        # check straight inside each suit with >=5 cards
         for suit, ranks in by_suit.items():
                 if royal.issubset(ranks):
                          
                          return True
         return False
                 
                 
                  i
                     
                     
                
            

        

                             

    def checkPlayer(self):
        pair = self.checkMatches()
        print(pair) 
        if self.checkPair(pair) == True:
            print(f"You have a pair of {pair[0]}")
        if self.checkTwoPair(pair) == True:
            print(f"You have a pair of {pair[0]} and {pair[1]}")
        if self.checkTrips(pair) == True:
            print(f"You have three of a kind of {pair[0]}")
        if self.checkQuads(pair) == True:
            print(f"You have four of a kind of {pair[0]}")
        if self.checkFullHouse(pair) == True:
            print("You have a full house")
        if self.checkFlush() == True:
            print("You have a flush")
        ''''
        if self.checkStraight() == True:
            print("You have a straight")
        '''
        if self.checkStraightFlush() == True:
            print("You have a straight flush")
        
    
    
        

poker = Game([], "", "Pre-Flop")

poker.player.dealCards(deck)
poker.dealer.dealCards(deck)
poker.currentRiver.dealFlop(deck)
poker.player.printCards()
poker.dealer.printDealerCards()
poker.currentRiver.printCards()
for i in range(2):
    poker.currentRiver.nextCard(deck)
poker.checkPlayer()






    
