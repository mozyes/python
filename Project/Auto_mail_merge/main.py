with open("Input/Letters/starting_letter.txt") as letter:
    sample_letter = letter.read()

with open("Input/Names/invited_names.txt") as people:
    all_people = people.read()
    all_person = all_people.split("\n")

for person in all_person:
    personal_letter = sample_letter.replace("[name]", person)
    with open(f"Output/ReadyToSend/{person}.txt", mode="w") as each_letter:
        each_letter.write(personal_letter)
