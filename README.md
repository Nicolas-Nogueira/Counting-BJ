# Counting-BJ
Building a Blackjack-playing agent that uses card counting to maximize winnings over 100 games. 

State sapce is the visible cards dealt(player’s hand, dealers up card), running count the true count based on observed cards, and the player’s bankroll and betting decisions. 

The start state is one shuffled 52 card deck, Player bankroll = $1000, and running count = 0


The successor function is dealing new cards, updating runnnig count, and agent making a move(hit/stand/double) and places a bet. 

The evaluation function is maximizing final bankroll after 100 rounds 

I set up bayesian reasoning by  using high-low strategy for Running count, the True count = running count/ cards remaining, and the Agent adjusts bet sizes based on true count. 

High-Low strtegy:
High cards: 
10,J,Q,K,A(good of player)
-1 to count value (player advantage goes down)

Low cards: 
2,3,4,5,6(good for dealer) 
+1 count(player advantage goes up)

Natural cards:
7,8,9
+0 count

I used Basic Strategy to minimize expected loss on each move(hit, stand, double)




 

