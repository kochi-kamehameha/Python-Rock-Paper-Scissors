# 🪨 Rock-Paper-Scissors (Python CLI)

A simple **command-line Rock-Paper-Scissors game** built with Python.  
Play against the computer, see the result instantly, and track your score across multiple rounds.

The game includes a clean terminal interface, emoji visuals, and a scoreboard that tracks your win rate.

---

# ✨ Features

## 🎮 Play Against the Computer
Challenge the computer in the classic game of **Rock, Paper, Scissors**.

Moves available:
- Rock 🪨
- Paper 📄
- Scissors ✂️

---

## ⌨️ Quick Input Shortcuts

You can enter moves using full words or shortcuts.

| Input | Move |
|------|------|
| rock | 🪨 Rock |
| paper | 📄 Paper |
| scissors | ✂️ Scissors |
| r | 🪨 Rock |
| p | 📄 Paper |
| s | ✂️ Scissors |

---

## 🤖 Computer Opponent

The computer randomly chooses its move each round using Python's `random` module.

---

## 📊 Score Tracking

After each round the game displays a scoreboard showing:

- Total rounds played
- Wins
- Losses
- Ties
- Win rate percentage

Example:

```
Rounds: 5 | Wins: 3 | Losses: 1 | Ties: 1 | Win rate: 60%
```

---

## 🧾 Round Result Display

Each round clearly shows both moves and the outcome.

Example:

```
You      → 🪨 Rock
Computer → ✂️ Scissors

YOU WIN! Rock beats Scissors
```

---

## 🔁 Multiple Rounds

After each round you can choose to:

- Continue playing
- End the game

At the end, the program shows **final results**.

---

# 📦 Requirements

Python **3.6 or higher**

This program only uses built-in Python libraries:

- `random`
- `time`

No additional installations are required.

---

# ▶️ How to Run

Save the script as:

```
rock_paper_scissors.py
```

Run it in your terminal:

```bash
python rock_paper_scissors.py
```

---

# 🎮 Example Gameplay

```
🪨 ROCK · PAPER · SCISSORS ✂️

Your move (rock/paper/scissors): rock

Computer is choosing...

You      → 🪨 Rock
Computer → ✂️ Scissors

YOU WIN! Rock beats Scissors

Rounds: 1 | Wins: 1 | Losses: 0 | Ties: 0 | Win rate: 100%
```

---

# ⚙️ How It Works

The game logic is based on three core components:

### Move System
A list stores all possible moves.

```
MOVES = ["rock", "paper", "scissors"]
```

---

### Win Logic

A dictionary defines which move defeats another.

```
BEATS = {
    "scissors": "paper",
    "paper": "rock",
    "rock": "scissors"
}
```

---

### Computer Move

The computer randomly selects a move each round.

```
random.choice(MOVES)
```
