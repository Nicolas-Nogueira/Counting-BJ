Blackjack Card-Counting AI

Overview
This project is a simulation of a Blackjack-playing agent that uses card-counting strategies to gain an advantage over the house. The goal is to demonstrate how the agent makes smarter bets using the High-Low counting method and whether it profits over time.

Project Components
Blackjack class: Simulates a Blackjack game, including dealing cards, evaluating hands, and determining game outcomes.

Agent class: Implements a Blackjack agent that plays using:

Basic Strategy (Hard Totals, Soft Totals, Pair Splits)

High-Low Card Counting System

Betting based on True Count

Data Visualization class: Plots the agent's betting patterns and profit trajectory over 100 games.

Strategy Details

Basic Strategy
The agent uses standard Blackjack decision rules:

Hard Totals (no Ace as 11)

Soft Totals (Ace as 11)

Pairs (splitting logic)

Card Counting: High-Low
Low cards (2–6): +1 to count

High cards (10–A): -1 to count

Neutral cards (7–9): 0 to count

Betting Strategy
The true count is calculated:
True Count = Running Count / Estimated Decks Remaining

The agent bets:

Minimum when count is low

Proportional to the true count when it's high

Simulation
The agent plays 100 Blackjack games

Results (bets and winnings) are tracked and visualized

Output
The program generates a graph showing:

Agent’s bet sizes per round

Agent’s cumulative profit/loss

Requirements
Python 3.x

matplotlib (for plotting)

No external data or internet access required

How to Run
Clone or download the repository.

Run the CountingBJ.py file.

View the resulting graph to assess the performance of the card-counting strategy.


 Notes
This project is educational and demonstrates a simplified version of real Blackjack gameplay.

It assumes a single player and fixed basic strategy.

No casino-specific rules (e.g. doubling after split, surrender) are currently implemented.




 

