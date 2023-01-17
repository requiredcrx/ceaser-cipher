#importing the needed modules
from alphabets import alphabet
from art import logo

#defining the functions
def ceaser(start_text, shift_number, cipher_type):
    #this condition get excecuted if the user wants to decode
    if cipher_type == "decode":
        shift_number *= -1
    
    #defining the loop that iterate in the list and shift the texts and creating an empty string
    ceaser_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_number
            new_letter = alphabet[new_position]
            ceaser_text += new_letter
        else:
            ceaser_text += char
    print(f"Here is the {cipher_type}d result: {ceaser_text}")

print(logo)

#creating a loop that allows user keep runing program as long as they want
end_cipher = False
while not end_cipher:
    direction = input("Type 'encode' to encrypt or type 'decode' to decrypt \n").lower()
    text = input("Type your message below \n").lower()
    shift = int(input("Enter a shift number \n"))

    #this prevent error if the user typed a shift number out of the list range
    shift = shift % 26

    #calling the function
    ceaser(start_text=text, shift_number=shift, cipher_type=direction)

    #This line prompts user to either continue using the program or exit
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no' \n").lower()
    if restart == "no":
        end_cipher = True
        print("Goodbye!")
    
