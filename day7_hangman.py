import random

word_list = ["aardvark", "baboon", "camel"]
word_length = len(word_list)
chosen_word = word_list[random.randint(0, word_length - 1)]
c = len(chosen_word)

print("Welcome to Hangman!")
print('''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'|| 
| |          || ||
| |          || ||
| |          || ||
| |         / | | \\
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .
''')

guess_word = []
for _ in range(c):
    guess_word.append("_")

guesses = 1
while guesses <= 6:
  print(" ".join(guess_word))
  user_letter = input("Guess a letter: ").lower()
  found = False
  for i, letter in enumerate(chosen_word):
    if user_letter == letter:
      guess_word[i] = letter
      found = True
  if not found:
    if guesses == 1:
      print('''
        +---+
        |   |
        O   |
            |
            |
            |
      =========
      ''')
    elif guesses == 2:
      print('''
        +---+
        |   |
        O   |
        |   |
            |
            |
      =========''')
    elif guesses == 3:
      print('''
        +---+
        |   |
        O   |
       /|   |
            |
            |
      =========''')
    elif guesses == 4:
      print('''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
      =========''')
    elif guesses == 5:
      print('''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
      =========''')
    elif guesses == 6:
      print('''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
      =========''')
    guesses += 1
    
print(" ".join(guess_word))
if '_' not in guess_word:
  print("Congratulations!!! You have guess word correctly.")
else:
  print("Gameover!!!")
