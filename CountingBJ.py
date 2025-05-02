import random 
# Main Program
def main():
    game = BlackjackGame()
    agent = Agent()
    data = DataCollector()
    
    for _ in range(1000):
        game.reset()
        agent.play_game(game)
        data.record(agent.current_bet, agent.bankroll)
    
    data.visualize_results()

# Blackjack Game Class
class BlackjackGame:
    def __init__(self):
        self.deck = self.create_shuffled_deck()
        self.dealer_hand = []
        self.player_hand = []
 
    def create_shuffled_deck(self):
        # Create and shuffle the deck
        deck = []
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        for value in values:
            for _ in range(4):
                deck.append(value)
        random.shuffle(deck)
        return deck

    def reset(self):
        # Reset the deck and deal initial hands
        self.deck = self.create_shuffled_deck()
        self.dealer_hand = []
        self.player_hand = []
        self.deal_initial_cards()

    def deal_initial_cards(self):
        # Deal two cards to dealer and player
        self.dealer_hand.append(self.deck.pop())
        self.dealer_hand.append(self.deck.pop())
        self.player_hand.append(self.deck.pop())
        self.player_hand.append(self.deck.pop())

    def deal_card(self, hand):
        # Give one card to hand
        card = self.deck.pop()
        hand.append(card)
        return hand

    def get_hand_value(self, hand):
        # Calculate value of a hand (account for Ace = 1 or 11)
        value = 0
        num_aces = 0

        for card in hand:
            if card in ['J', 'Q', 'K']:
                value += 10
            elif card == 'A':
                value += 11
                num_aces += 1
            else:
                value += card

        # If value > 21 and hand has Aces, reduce value by 10 per Ace
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1

        return value

    def dealer_turn(self):
        # Dealer hits according to rules (typically until 17+)
        while self.get_hand_value(self.dealer_hand) < 17:
            self.deal_card(self.dealer_hand) 

    def is_blackjack(self, hand):
        # Return True if hand is a blackjack
        if self.get_hand_value(hand) == 21:
            return True
        return False

    def is_bust(self, hand):
        # Return True if hand value > 21
        if self.get_hand_value(hand) > 21:
            return True
        return False

def test_blackjack_game():
    game = BlackjackGame()

    # Test 1: Check deck has 52 cards
    print("Test 1: Deck has 52 cards:", len(game.deck) == 52)

    # Test 2: Deal initial cards
    game.deal_initial_cards()
    print("Test 2: Player and dealer have 2 cards each:",
          len(game.player_hand) == 2 and len(game.dealer_hand) == 2)

    # Test 3: Check card values (hand with known cards)
    test_hand = [10, 'K']  # Total should be 20
    print("Test 3: Hand value should be 20:", game.get_hand_value(test_hand) == 20)

    test_hand = [5, 'A']  # Should be 16
    print("Test 3.1: Hand value should be 16:", game.get_hand_value(test_hand) == 16)

    test_hand = [5, 'A', 'A']  # Should be 17
    print("Test 3.2: Hand value should be 17:", game.get_hand_value(test_hand) == 17)

    # Test 4: Check blackjack detection
    blackjack_hand = [10, 'A']
    print("Test 4: Is blackjack:", game.is_blackjack(blackjack_hand))

    # Test 5: Check bust detection
    bust_hand = [10, 9, 5]
    print("Test 5: Is bust:", game.is_bust(bust_hand))

    # Test 6: Dealer hits until 17+
    game.reset()
    game.dealer_hand = [2, 3]  # Force weak hand
    game.dealer_turn()
    dealer_total = game.get_hand_value(game.dealer_hand)
    print("Test 6: Dealer stops at 17 or more:", dealer_total >= 17)

# Run the test
test_blackjack_game()

# Agent Class
class Agent:
    def __init__(self):
        self.running_count = 0
        self.true_count = 0
        self.betting_unit = 25
        self.bankroll = 1000  # starting money
        self.current_bet = 0

    def update_running_count(self, cards_seen):
        # Update count based on high-low system
        for card in cards_seen:
            if card in [2,3,4,5,6]:
                self.running_count += 1
            elif card in [10,'J','Q','K','A']:
                self.running_count -= 1

    def calculate_true_count(self, decks_remaining):
        # True Count = Running Count / Decks Remaining
        self.true_count = self.running_count / decks_remaining

    def place_bet(self):
        # Betting strategy based on true count
        if self.true_count >= 2:
            self.current_bet = self.betting_unit * (self.true_count - 1)
        else:
            self.current_bet = self.betting_unit

    def decide_move(self, player_hand, dealer_card):
        # Implement Basic Strategy rules
        player_value = BlackjackGame().get_hand_value(BlackjackGame().player_hand)
        dealer_value = BlackjackGame().get_hand_value(BlackjackGame().dealer_hand[0])#dealers upcard
        can_double = len(player_hand) == 2 

         #soft total 
        while player_value[0] or  player_value[1] == 11:
            if player_value <= 17: 
                return 'double' if can_double and 3 <= dealer_value <=6 else 'hit'
            elif player_value == 18:
                return 'double' if can_double else 'stand'
            elif dealer_value in [2,7,8]:
                return 'stand'
            else: # Soft 19 or more
                return 'hit'
            

        #hard total 
        if player_value <= 9 :
            return 'double' if can_double and 3 <= dealer_value <=6 else 'hit'
        elif player_value == 10 :
            return 'double' if can_double and dealer_value <= 9 else 'hit'
        elif player_value == 11:
            return 'double' if can_double else 'hit' 
        elif player_value == 12:
            return 'stand' if can_double and dealer_value in [4,5,6] else 'hit'
        elif player_value in [13,14,15,16]:
            return 'stand' if can_double and dealer_value in range(2,6) else 'hit'
        else:
            return 'stand'




    def play_game(self, game):
        # Play one game using counting and basic strategy
        self.place_bet()
        # Play moves based on strategy
        # Update counts after seeing new cards
        # Determine win or loss
        # Update bankroll accordingly
        pass

# Data Collector Class
class DataCollector:
    def __init__(self):
        self.bets = []
        self.profits = []

    def record(self, bet, bankroll):
        self.bets.append(bet)
        self.profits.append(bankroll)

    def visualize_results(self):
        # Use matplotlib or similar to plot bankroll over games
        pass

# Run the program
if __name__ == "__main__":
    main()

    
    





                


        

        

