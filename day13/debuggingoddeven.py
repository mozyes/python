number = int(input("Which number do you want to check?"))
# issue was number % 2 = 0 and issue solved by ==, because we are comparing not assigning.
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
