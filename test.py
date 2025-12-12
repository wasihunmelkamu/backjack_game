import random
import tkinter as tk
from tkinter import messagebox

# -------- GAME LOGIC --------
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

# -------- UI LOGIC --------
def start_game():
    global user_cards, computer_cards, game_over
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    game_over = False
    update_ui()

def hit():
    global game_over
    if not game_over:
        user_cards.append(deal_card())
        update_ui()
        if calculate_score(user_cards) > 21:
            end_game()

def stand():
    end_game()

def end_game():
    global game_over
    game_over = True

    while calculate_score(computer_cards) < 17 and calculate_score(computer_cards) != 0:
        computer_cards.append(deal_card())

    result = compare(
        calculate_score(user_cards),
        calculate_score(computer_cards)
    )

    messagebox.showinfo("Game Over", result)
    update_ui(show_all=True)

def update_ui(show_all=False):
    user_score = calculate_score(user_cards)

    user_label.config(text=f"Your Cards: {user_cards} | Score: {user_score}")

    if show_all:
        comp_score = calculate_score(computer_cards)
        computer_label.config(text=f"Computer Cards: {computer_cards} | Score: {comp_score}")
    else:
        computer_label.config(text=f"Computer First Card: {computer_cards[0]}")

# -------- TKINTER UI --------
root = tk.Tk()
root.title("Blackjack")

user_label = tk.Label(root, text="Your Cards: []", font=("Arial", 12))
user_label.pack(pady=10)

computer_label = tk.Label(root, text="Computer Cards: []", font=("Arial", 12))
computer_label.pack(pady=10)

tk.Button(root, text="Start Game", width=15, command=start_game).pack(pady=5)
tk.Button(root, text="Hit", width=15, command=hit).pack(pady=5)
tk.Button(root, text="Stand", width=15, command=stand).pack(pady=5)

root.mainloop()
