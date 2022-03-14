alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(message, number):
  cipher = ""
  for letter in message:
    position = alphabet.index(letter)
    new_position = position + number
    new_letter = alphabet[new_position]
    cipher += new_letter
  print(f"The encoded text is {cipher}")

def decrypt(cipher, number):
  plain_text =""
  for letter in cipher:
    position = alphabet.index(letter)
    new_position = position - number
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}") 

if direction == "encode":
  encrypt(message=text, number=shift)
elif direction =="decode":
  decrypt(cipher=text, number=shift)
  