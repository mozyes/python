from replit import clear
#HINT: You can call clear() to clear the output in the console.
from artauction import logo
print(logo)
print("Welcome to the secret auction program.")
redo = True
auction = {}
while redo:
    name = input("what is your name?: ")
    bid_ammount = int(input("What's your bid?: $"))
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders.lower() == "yes":
      clear()
    else:
      redo = False
    auction[name] = bid_ammount


clear()
highest_bid = 0
winner = ""
for client in auction:
  bidded_ammount = auction[client]
  if bidded_ammount > highest_bid:
    highest_bid = bidded_ammount
    winner = client


print(f"The winner is {winner} with a bid of ${highest_bid}")
