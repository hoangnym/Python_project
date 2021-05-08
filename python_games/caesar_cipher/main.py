alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):

    encrypted = ''
    for letter in text:
        idx_o = alphabet.index(letter)
        idx_s = idx_o + shift

        ##Account for out of range error
        if idx_s >= 26:
            idx_s -= 26

        encrypted += alphabet[idx_s]
    
    print(f"The encypted text is {encrypted}.")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):

    decrypted = ''
    for letter in text:
        idx_o = alphabet.index(letter)
        idx_s = idx_o - shift

        ## Account for out of range error
        if idx_s < 0:
            idx_s += 26

        decrypted += alphabet[idx_s]

    print(f"The decrypted text is {decrypted}.")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. 
#Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)

