import random
print("Welcome to Rock Paper Scissors game")
user_choice = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ')
computer_choice = random.randint(0,2)
if int(user_choice) == 0:
    print("""
    You chose: 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif int(user_choice) == 1:
    print("""
    You chose:
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else:
    print("""
    You chose:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
if int(computer_choice) == 0:
    print("""
    computer chose: 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif int(computer_choice) == 1:
    print("""
    Computer chose:
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else:
    print("""
    Computer chose:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
if computer_choice - int(user_choice) == 1:
    print("You loose!!!")
elif computer_choice == int(user_choice):
    print("its a draw!!!")
else:
    print("You won!!!")
