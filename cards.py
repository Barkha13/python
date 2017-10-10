from random import shuffle

class Card (object):
    def __init__(self,suite,value):
        self.suite = suite
        self.value = value
        # self.card = card

class Deck(object):
    def __init__(self):
    # def createdeck(self):
        self.deck_list = []
        self.value_list = []
        for i in range(1,14):
            self.value_list.append(i)   
        self.suites = ["spades","diamond","heart","clubs"] 
            
        for i in self.suites:
            for j in self.value_list:
                self.deck_list.append(Card(i,j))
    # print deck_list[15].value ,"-" ,deck_list[15].suite

    def shuffle_deck(self,deck_list):
        shuffle(deck_list)
        return self
  
    # def draw_card(self):
    #     self.deck_list.remove(
    

class User(object): 
    def __init__(self,name):
        self.name =name 
        self.total = 0
        self.hand = []
    
    def draw_card(self,deck_list):
        # print deck_list
        last = deck_list.pop()
        self.hand.append(last)
        last_value = last.value
        print "You got",last_value
        
        # print last
        # print self.hand[0].value ,"-", self.hand[0].suite
        self.total = self.total + last_value
        print "Total",self.total
        if self.total > 21:
            self.total = 0
            print "You Lose"
            return  0
            
        else:
            print "Draw card?"
            return 1
       

user1 = User("dave")
deck = Deck()

cards = Deck()
cards.shuffle_deck(deck.deck_list)
result = user1.draw_card(deck.deck_list)
while result == 1:
    user1.draw_card(deck.deck_list)
    break
print "Game Over"
   

        

        