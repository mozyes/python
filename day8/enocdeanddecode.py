alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
  encrypted_word = ""
  for letter in text:
    for i, char in enumerate(alphabet):
      if letter == char:
        shifted_location = i + shift
        if shifted_location > 25:
          shifted_location -= 26
        encrypted_word += alphabet[shifted_location]
  print(encrypted_word)

def decrypt(text, shift):
  decrypted_word = ""
  for letter in text:
    for i, char in enumerate(alphabet):
      if letter == char:
        shifted_location = i - shift
        if shifted_location < 0:
          shifted_location += 26
        decrypted_word += alphabet[shifted_location]
  print(decrypted_word)

counter = 0
while counter == 0:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  if direction.lower() == "encode":
    encrypt(text, shift)
  elif direction.lower() == "decode":
    decrypt(text, shift)
  try_again = input("do you want to try again?\n")
  if try_again.lower() == "n" or try_again.lower() == "no":
    counter += 1 
