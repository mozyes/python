# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_person = len(names)
choice = random.randint(1,len(names))
names_pay = names[choice - 1]
print(f"{names_pay} is going to buy the meal today!")
