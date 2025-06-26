'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    if letter == " ":
        return " "
    else:
        X = (ord(letter) - ord('A') + shift) % 26
        return chr(ord('A') + X)

def caesar_cipher(message, shift):
     output = ""
     for i in message:
        if i == " ":
            output += " "
        else:
            x = (ord(i) - ord('A') + shift) % 26 + ord('A')
            output += chr(x)
     return output

def shift_by_letter(letter, letter_shift):
    if letter == " ":
         return " "
    else:
         X = (ord(letter) - ord('A') + (ord(letter_shift)-ord('A'))) % 26
         return chr(ord('A') + X)

def vigenere_cipher(message, key):
    result = ""
    Y = 0

    for i in message:
        if i == ' ':
            result += i
        else:
            shift = ord(key[Y % len(key)]) - ord('A')
            X = chr((ord(i) - ord('A') + shift) % 26 + ord('A'))
            result += X
        Y += 1  

    return result

def scytale_cipher(message, shift):
    if len(message)%shift!=0:
        message += "_" * (shift - (len(message) % shift))

    output= ""
    n=len(message)

    for i in range(n):
        position= (i//shift)+((n//shift)*(i % shift))
        output += message[position]
    return output
     
def scytale_decipher(message, shift): 
    output=""
    n=len(message)
    for i in range(n):
        position = (i %(n//shift)) * shift + (i // (n//shift))
        output += message[position]
    return output