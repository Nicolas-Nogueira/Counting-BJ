import random 
import matplotlib.pyplot as plt

# Main Program
def main():
    game = BlackjackGame()
    agent = Agent()
    data = DataCollector()
    

    for _ in range(100):
        game.reset()
        agent.play_game(game)
        data.record(agent.current_bet, agent.bankroll)
    
    data.visualize_results()

# Blackjack Game Class
class BlackjackGame:
    def __init__(self, num_decks=6, penetration_limit=0.75):
        self.num_decks = num_decks
        self.penetration_limit = penetration_limit  # % of cards dealt before reshuffle
        self.total_cards = 52 * self.num_decks
        self.cards_dealt = 0
        self.deck = self.create_shuffled_deck()
        self.dealer_hand = []
        self.player_hand = []

    def create_shuffled_deck(self):
        deck = []
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        for _ in range(self.num_decks):
            for value in values:
                for _ in range(4):
                    deck.append(value)
        random.shuffle(deck)
        self.cards_dealt = 0  # reset counter on new deck
        return deck

    def reset(self):
        # Check if we need to reshuffle based on penetration
        if self.cards_dealt > self.total_cards * self.penetration_limit:
            print("Reshuffling shoe (penetration limit reached)...")
            self.deck = self.create_shuffled_deck()
        
        self.dealer_hand = []
        self.player_hand = []
        self.deal_initial_cards()

    def deal_card(self, hand):
        card = self.deck.pop()
        self.cards_dealt += 1
        hand.append(card)
        return card

    def deal_initial_cards(self):
        self.deal_card(self.dealer_hand)
        self.deal_card(self.dealer_hand)
        self.deal_card(self.player_hand)
        self.deal_card(self.player_hand)

    def get_hand_value(self, hand):
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
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1
        return value

    def dealer_turn(self):
        while self.get_hand_value(self.dealer_hand) < 17:
            self.deal_card(self.dealer_hand)

    def is_blackjack(self, hand):
        return self.get_hand_value(hand) == 21 and len(hand) == 2

    def is_bust(self, hand):
        return self.get_hand_value(hand) > 21

    def get_decks_remaining(self):
        return max(1, len(self.deck) / 52.0)  # avoid divide-by-zero


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
        self.bankroll = 500 # starting money
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
            self.current_bet = min(self.betting_unit * (self.true_count - 1), self.bankroll, 250)
        else:
            self.current_bet = min(self.betting_unit, self.bankroll)

    def decide_move(self, player_hand, dealer_card):
        # Implement Basic Strategy rules
        player_val = BlackjackGame().get_hand_value(player_hand)
        dealer_val = BlackjackGame().get_hand_value([dealer_card])
        can_double = len(player_hand) == 2 

               #hard total 
        if player_val <= 9 :
            return 'double' if can_double and 3 <= dealer_val <=6 else 'hit'
        elif player_val == 10 :
            return 'double' if can_double and dealer_val <= 9 else 'hit'
        elif player_val == 11:
            return 'double' if can_double else 'hit' 
        elif player_val == 12:
            return 'stand' if can_double and dealer_val in [4,5,6] else 'hit'
        elif player_val in [13,14,15,16]:
            return 'stand' if can_double and dealer_val in range(2,6) else 'hit'
        else:
            return 'stand'

    def play_game(self, game):
        # initial setup 
        print("Starting new game round...")
        
        self.place_bet()
        bet = self.current_bet
        print(f"Bet placed: ${bet:.2f}")
        print(f" Running count: {self.running_count}, True count: {self.true_count:.2f}")
        print(f"Bankroll before round: ${self.bankroll:.2f}")
        
        # Deal initial cards
        dealer_card = game.dealer_hand[0]
        print(f" Player hand: {game.player_hand}, value: {game.get_hand_value(game.player_hand)}")
        print(f" Dealer upcard: {dealer_card}")

        move = self.decide_move(game.player_hand, dealer_card)
        
        if move == 'hit':
            game.deal_card(game.player_hand)
            print(f" Player hits and receives: {game.player_hand[-1]}")
        elif move == 'double':
            bet = min(bet * 2, self.bankroll)
            game.deal_card(game.player_hand)
            print(f"Player doubles! New card: {game.player_hand[-1]}")
            print(f"New bet amount: ${bet:.2f}")
        else: 
            print("Player stands.")

        print(f" Final player hand: {game.player_hand}, value: {game.get_hand_value(game.player_hand)}")

        #dealer turn 
        game.dealer_turn()
        print(f" Dealer final hand: {game.dealer_hand}, value: {game.get_hand_value(game.dealer_hand)}")

        # Calculate final values
        player_value = game.get_hand_value(game.player_hand)
        dealer_value = game.get_hand_value(game.dealer_hand)
    
        #outcome
        if game.is_bust(game.player_hand):
            payout = -bet
            print("Player busted.")
        elif game.is_bust(game.dealer_hand):
            payout = bet
            print("Dealer busted. Player wins!")
        elif game.is_blackjack(game.player_hand) and not game.is_blackjack(game.dealer_hand):
            payout = bet * 1.5  # Blackjack pays 3:2
            print("Blackjack! Player wins!")
        elif player_value > dealer_value:
            payout = bet  
            print("Player wins.")
        elif player_value < dealer_value:
            payout = -bet
            print("Dealer wins.")
        else:
            payout = 0
            print("Push (tie).")
        
        # Update bankroll
        self.bankroll += payout
        print(f"Bankroll after round: ${self.bankroll:.2f}")

        # Update card counting
        cards_seen = game.player_hand + game.dealer_hand
        self.update_running_count(cards_seen)
        self.calculate_true_count(game.get_decks_remaining())
        print(f"Updated running count: {self.running_count}, True count: {self.true_count:.2f}")

# Data Collector Class
class DataCollector:
    def __init__(self):
        self.bets = []
        self.profits = []

    def record(self, bet, bankroll):
        self.bets.append(bet)
        self.profits.append(bankroll)

    def visualize_results(self):
        rounds = list(range(1, len(self.bets) + 1))
        # Plot 1: Bankroll over time
        plt.figure(figsize=(12, 5))

        plt.subplot(1, 2, 1)
        plt.plot(rounds, self.profits, label='Bankroll', color='green')
        plt.xlabel('Round')
        plt.ylabel('Bankroll ($)')
        plt.title('Bankroll Over Time')
        plt.grid(True)
        plt.legend()

        # Plot 2: Bet size per round
        plt.subplot(1, 2, 2)
        plt.plot(rounds, self.bets, label='Bet Size', color='blue')
        plt.xlabel('Round')
        plt.ylabel('Bet Amount ($)')
        plt.title('Bet Size Per Round')
        plt.grid(True)
        plt.legend()

        plt.tight_layout()
        plt.show()


# Run the program
if __name__ == "__main__":
    main()

    
    





                


        

        

