Overview
This Python script simulates a series of Blackjack games to compare the performance of two different agents: a Counting Agent and a Random Agent. The Counting Agent uses card counting strategies to make decisions, while the Random Agent makes decisions randomly. The script collects data on the bankrolls of both agents over multiple games and visualizes the results.

Dependencies
Python 3.x
matplotlib for plotting results
You can install the required library using pip:


Script Structure
Main Program
The main() function initializes the game and agents, runs the simulation for 100 rounds, and visualizes the results.

Classes
BlackjackGame
This class represents the Blackjack game itself. It includes methods for creating and shuffling the deck, dealing cards, calculating hand values, and managing the dealer's turn.

CountingAgent
This class represents the agent that uses card counting strategies. It includes methods for updating the running count, calculating the true count, placing bets, deciding moves based on basic strategy rules, and playing a game round.

RandomAgent
This class represents the agent that makes random decisions. It includes methods for placing bets, deciding moves randomly, and playing a game round.

DataCollector
This class collects and visualizes the bankroll data of both agents. It includes methods for recording bankrolls and plotting the results.

Functions
test_blackjack_game()
This function runs a series of tests on the BlackjackGame class to ensure its methods work correctly.

How to Run
Ensure you have Python 3.x installed.
Install the required library (matplotlib) using pip.
Run the script:

The script will simulate 100 rounds of Blackjack, comparing the performance of the Counting Agent and the Random Agent, and then visualize the results in a plot.




 

