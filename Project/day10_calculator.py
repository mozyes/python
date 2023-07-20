from replit import clear
from artcalc import logo

def calculations(first, next, operation):
  result = 0
  if operation == "+":
    result = first + next
  elif operation == "-":
    result = first - next
  elif operation == "*":
    result = first * next
  elif operation == "/":
    result = first / next
  return result

redo = False
while not redo:
  print(logo)
  first_number = float(input("What's the first number?: "))
  redo = True
  while redo:
    print("+\n-\n*\n/\n")
    operation = input("Pick an operation: ")
    next_number = float(input("What's the next number?: "))
    final_result = calculations(first_number, next_number, operation)
    print(f"{first_number} {operation} {next_number} = {final_result}")
    more_program = input(f"Type 'y' to continue calculating with {final_result} or type 'n' to start a new calulation: ").lower()
    if more_program == "y":
      redo = True
      first_number = final_result
    else:
      redo = False
      clear()

  
