import random
from replit import clear
from artblackjack import logo

total_cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}

def deal_card():
    """Returns a random card from the deck."""
    cards = list(total_cards.keys())
    return random.choice(cards)

def calculate_points(cards):
    """Calculate the total value of a hand of cards."""
    total_point = sum(total_cards[score] for score in cards)
    a_counter = cards.count("A")
    
    while total_point > 21 and a_counter > 0:
        total_point -= 10
        a_counter -= 1

    return total_point

def play_game():
    global a_counter  # Declare a_counter as a global variable
    print("Welcome to Blackjack")
    player_cards = []
    dealer_cards = []
    is_game_over = False
    
    for deal in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())
    
    print(f"Your cards: {player_cards}")
    print(f"Dealer's first card: {dealer_cards[0]}")
    redo = True
    player_points = calculate_points(player_cards)  # Initialize player_points
    while redo:
        choice = input("Do you want another card? (y/n): ").lower()
        if choice == "y":
            player_cards.append(deal_card())
            print(f"Your cards: {player_cards}")
            player_points = calculate_points(player_cards)
            if player_points > 21:
                print("Bust! You lose.")
                redo = False
        else:
            redo = False
    
    dealer_points = calculate_points(dealer_cards)
    print(f"Your final hand: {player_cards}, final score: {player_points}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_points}")
    
    # Dealer's turn
    while dealer_points < 17:
        dealer_cards.append(deal_card())
        dealer_points = calculate_points(dealer_cards)
        print(f"Dealer drew a new card: {dealer_cards[-1]}, new score: {dealer_points}")
    
    if not redo:
        if dealer_points > 21:
            print("Dealer busts! You win!")
        elif dealer_points == player_points:
            print("It's a draw!")
        elif dealer_points > player_points:
            print("Dealer wins!")
        else:
            print("You win!")

a_counter = 0  # Initialize a_counter outside the function

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    clear()
    print(logo)
    play_game()
