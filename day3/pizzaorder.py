# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            total = 15 + 2 + 1
        else:
            total = 15 + 2
    else:
        if extra_cheese == "Y":
            total = 15 + 1
        else:
            total = 15
if size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            total = 20 + 3 + 1
        else:
            total = 20 + 3
    else:
        if extra_cheese == "Y":
            total = 20 + 1
        else:
            total = 20
if size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            total = 25 + 3 + 1
        else:
            total = 25 + 3
    else:
        if extra_cheese == "Y":
            total = 25 + 1
        else:
            total = 25
print(f"Your final bill is: ${total}.")
