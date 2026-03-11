# Rock-Paper-Scissors 🪨📄✂️
# Play against the computer. Type your move, see results instantly, track your score.

import random
import time

MOVES = ["rock", "paper", "scissors"]
EMOJI = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
BEATS = {"scissors": "paper", "paper": "rock", "rock": "scissors"}

def separator(char="─", width=50):
    print(char * width)

def banner():
    separator("═")
    print("   🪨 ROCK · PAPER · SCISSORS ✂️")
    separator("═")
    print("  Challenge the computer! Shortcuts: r/p/s")
    separator("═")
    print()

def get_player_move():
    shortcuts = {"r": "rock", "p": "paper", "s": "scissors"}
    while True:
        raw = input("Your move (rock/paper/scissors): ").strip().lower()
        move = shortcuts.get(raw, raw)
        if move in MOVES:
            return move
        print("Invalid input. Try rock/paper/scissors (or r/p/s).")

def get_computer_move():
    return random.choice(MOVES)

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif BEATS[player] == computer:
        return "win"
    else:
        return "loss"

def show_round_result(player, computer, result):
    print()
    separator("·")
    print(f"You      → {EMOJI[player]} {player.capitalize()}")
    print(f"Computer → {EMOJI[computer]} {computer.capitalize()}")
    separator("·")
    if result == "tie":
        print("It's a TIE! No points.")
    elif result == "win":
        print(f"YOU WIN! {player.capitalize()} beats {computer.capitalize()}")
    else:
        print(f"YOU LOSE! {computer.capitalize()} beats {player.capitalize()}")

def show_scoreboard(wins, losses, ties):
    total = wins + losses + ties
    win_rate = round((wins / total) * 100) if total else 0
    print()
    separator()
    print(f"Rounds: {total} | Wins: {wins} | Losses: {losses} | Ties: {ties} | Win rate: {win_rate}%")
    separator()

def show_final_message(wins, losses, ties):
    total = wins + losses + ties
    print()
    separator("═")
    print("GAME OVER — FINAL RESULTS")
    separator("═")
    if total == 0:
        print("You didn't play any rounds.")
    else:
        win_rate = round((wins / total) * 100)
        print(f"Played {total} rounds. Wins: {wins} ({win_rate}%)")
        if wins > losses:
            print("🏆 You beat the computer!")
        elif losses > wins:
            print("🤖 The computer beat you!")
        else:
            print("🤝 Perfectly matched!")
    separator("═")
    print("Thanks for playing! 👋")
    separator("═")
    print()

def play():
    banner()
    wins = losses = ties = 0

    while True:
        print("─── New Round ───")
        player_move = get_player_move()

        print("Computer is choosing", end="", flush=True)
        for _ in range(3):
            time.sleep(0.35)
            print(".", end="", flush=True)
        print()

        computer_move = get_computer_move()
        result = determine_winner(player_move, computer_move)

        if result == "win":
            wins += 1
        elif result == "loss":
            losses += 1
        else:
            ties += 1

        show_round_result(player_move, computer_move, result)
        show_scoreboard(wins, losses, ties)

        again = input("Play another round? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            break
        print()

    show_final_message(wins, losses, ties)

if __name__ == "__main__":
    play()