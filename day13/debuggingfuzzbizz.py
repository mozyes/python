#the issue was in coding coz the number should be divisible by both 3 and 15 to be fizzbuzz and also the [] in last print statement. also another issue was it didnt have elif, coz the condition for all should print only 1 but as there were multiple statement, it went through all if statement

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
