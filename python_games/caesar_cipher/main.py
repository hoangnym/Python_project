from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#Create caesar function
def caesar(text, shift, direction):

    caesar = ''
    for char in text:
        if char in alphabet:
            idx_o = alphabet.index(char)

            if direction == "encode":
                idx_s = idx_o + shift
                ##Account for out of range error
                while idx_s >= 26:
                    idx_s -= 26
                caesar += alphabet[idx_s]
            elif direction == "decode":
                idx_s = idx_o - shift
                ## Account for out of range error
                while idx_s < 0:
                    idx_s += 26

                caesar += alphabet[idx_s]
        else:
            caesar += char
    
    print(f"The {direction}d text is {caesar}.")


if __name__ == "__main__":
    print(logo)

    want_to_continue = True

    while want_to_continue:
        go_again = input("Do you want to go again, yes or no? \n").lower()
        if go_again == "yes":
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            caesar(text, shift, direction)
        elif go_again == "no":
            want_to_continue = False



