# Blackjack Agent Simulator

A Python simulation that compares the performance of two blackjack-playing agents over multiple rounds: a **Counting Agent** that uses card counting strategies and a **Random Agent** that makes decisions randomly. The project tracks their bankrolls over time and provides a visual analysis of their performance.

## Features

- Simulates 100 rounds of Blackjack gameplay
- **Counting Agent**: Implements card counting strategy for informed decision-making
- **Random Agent**: Makes random decisions as a baseline comparison
- Real-time bankroll tracking for both agents
- Data visualization showing performance trends over time
- Comprehensive test suite for game logic validation

## Technologies Used

- **Python 3.x** - Core programming language
- **matplotlib** - Data visualization and plotting

## Installation

1. Clone the repository:
```bash
   git clone repo-link
   cd blackjack-agent-simulator
```

2. Install required dependencies:
```bash
   pip install matplotlib
```

## Usage

Run the main simulation script:
```bash
python main.py
```

This will simulate 100 rounds of Blackjack and generate a visualization comparing the bankroll performance of both agents over time.

## Running Tests

Execute the test suite to verify game logic:
```bash
python -m pytest tests/
```

## Project Structure
```
blackjack-agent-simulator/
├── main.py                 # Main simulation script
├── agents/                 # Agent implementations
│   ├── counting_agent.py
│   └── random_agent.py
├── game/                   # Blackjack game logic
└── tests/                  # Test files
```

## How It Works

The Counting Agent uses card counting techniques to track the ratio of high to low cards remaining in the deck, adjusting its strategy accordingly. The Random Agent serves as a control, making decisions without any strategic consideration. By comparing their performance over multiple rounds, the simulation demonstrates the effectiveness of card counting strategies.

## Results

### Bankroll Performance Over Time

<img width="468" height="281" alt="Bankroll comparison between Counting Agent and Random Agent" src="https://github.com/user-attachments/assets/5e84758c-1438-4018-9b78-bee18fb9e776" />

### Individual Agent Performance

<img width="468" height="195" alt="Counting Agent bankroll over time" src="https://github.com/user-attachments/assets/52d0611b-10ba-4f1e-b039-8fafce6b333c" />

<img width="468" height="195" alt="Random Agent bankroll over time" src="https://github.com/user-attachments/assets/fb102684-90b4-415e-8015-11974a0c5f11" />

## Findings

Based on the simulation results:

- **Counting Agent Performance**: The Counting Agent demonstrates more consistent and strategic gameplay, leveraging card counting to make informed decisions about hitting, standing, and betting. The bankroll trend shows the impact of strategic decision-making over random chance.

- **Random Agent Performance**: The Random Agent's bankroll exhibits higher volatility due to the lack of strategic decision-making. Without card counting or basic strategy, the agent's performance relies purely on luck.

- **Comparative Analysis**: When comparing both agents side-by-side, the data illustrates how card counting strategies can influence long-term outcomes in Blackjack. The visualization clearly shows the divergence in bankroll trajectories between strategic and random play.

- **Key Insights**:
  - Card counting provides a measurable advantage over random decision-making
  - Bankroll volatility is significantly reduced with strategic play
  - The house edge remains a factor even with card counting, as seen in overall trends
  - Random decision-making leads to unpredictable and generally unfavorable outcomes

## Future Enhancements

- Add more sophisticated agent strategies (Basic Strategy, Hi-Lo counting variations)
- Implement configurable simulation parameters (rounds, starting bankroll, betting limits)
- Export results to CSV for further analysis
- Add real-time progress display
- Include statistical analysis (win rate, average bet size, standard deviation)
- Implement multiple deck simulations











 

