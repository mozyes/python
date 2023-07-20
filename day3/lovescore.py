# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combine_string = name1 + name2
low_case = combine_string.lower()

t = low_case.count("t")
r = low_case.count("r")
u = low_case.count("u")
e = low_case.count("e")

true = t + r + u + e

l = low_case.count("l")
o = low_case.count("o")
v = low_case.count("v")
e = low_case.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) >= 40 and int(love_score) <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
