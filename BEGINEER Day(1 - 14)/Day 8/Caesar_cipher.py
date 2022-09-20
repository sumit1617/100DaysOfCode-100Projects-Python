import cipher_logo
print(cipher_logo.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]




def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position =  alphabet.index(char)
            if cipher_direction == "decode":
                new_position = position - shift_amount
            else:
                new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char    
    print(f"Here's the {cipher_direction}d result: {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type you message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26


    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'Yes' if you want to go again. Otherwise type 'No'.\n").lower()
    if result == 'no':
        should_continue = False
        print("Goodbye!.")



# The below one is by taking ony by one function
# def decrpyt(cipher_text, shift_amount):
#         plain_text = ""
#         for letter in cipher_text:
#             position = alphabet.index(letter)
#             new_position = position - shift_amount
#             new_letter = alphabet[new_position]
#             plain_text += new_letter
    
#         print(f"The decoded text is {plain_text}")

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter

#     print(f"The encoded text is {cipher_text}")
