def greet_with(name, location):
  print(f"Welcome {name}")
  print(f"What is it like in {location}?")

person_name = input("What is your name? ")
person_location = input("Where are you from? ")
greet_with(person_name, person_location)

#the position of the parameter and argument determines which  input goes where. suppose greet_with(person_location, person_name) then the output will have location of the person in name parameter and name in location parameter.
