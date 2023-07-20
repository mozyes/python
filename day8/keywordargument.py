def greet_with(name, location):
  print(f"Welcome {name}")
  print(f"What is it like in {location}?")

person_name = input("What is your name? ")
person_location = input("Where are you from? ")
greet_with(name = person_name, location = person_location)

#Now even if i change location in greet_with in 1st position, the output will be location parameter only!
