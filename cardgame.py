import random

card_deck = 10
player_won_score = (card_deck / 2) + 1

class Player:
    def __init__(self,name):
        self.name = name
        self.points = 0
        self.cards = list(range(1, card_deck + 1, 1))
        
        random.shuffle(self.cards)
    
    def pick_card(self):
        picked_card = self.cards[0]
        self.cards.remove(picked_card)
        print(f"{self.name} card is {picked_card}")
        return picked_card
    
    def add_point(self):
        self.points += 1
        print(f"A point has been added to the player: {self.name}")

    def game_over(self):
        return len(self.cards) == 0 or self.points == player_won_score     

player1 = Player(name="Player1")
player2 = Player(name="Player2")

print("The Game has been started!")
while True:
    input("Press Enter to pick a card!")
    player1_card = player1.pick_card()
    player2_card = player2.pick_card()
    if player1_card > player1_card:
        player1.add_point()
    elif  player2_card > player1_card:
         player2.add_point()
    else:
        print("IT'S A TIE")

    if player1.game_over() or player2.game_over():
        print("GAME OVER!")
        if player1.points > player2.points:
            print(f"{player1.name} wins!")
        elif player2.points > player1.points:
            print(f"{player2.name} wins!")
        else:
            print(f"THE SCORE IS A TIE")
        
        print(f"FINAL SCORE: {player1.points} - {player2.points}")
        break

    print(f"SCORE: {player1.points} - {player2.points}")