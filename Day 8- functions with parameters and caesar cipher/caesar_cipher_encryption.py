alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(message, number):
  encrypt_message = ""
  for letter in message:
    position = alphabet.index(letter)
    new_position = position + number
    new_letter = alphabet[new_position]
    encrypt_message += new_letter
  print(f"The encoded text is {encrypt_message}")

encrypt(message=text, number=shift)