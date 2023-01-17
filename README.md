# Ceaser Cipher
This is a Python program that implements the Ceaser Cipher encryption and decryption algorithm. The program prompts the user to either encrypt or decrypt a message, then prompts for the message and a shift value. It then uses the shift value to shift the letters of the message by the specified amount and print the resulting encoded or decoded message to the console.

## Usage
To run the program, simply execute the ceaser_cipher.py script in a Python environment. The program will prompt the user to either encrypt or decrypt a message, then prompts for the message and a shift value. It then uses the shift value to shift the letters of the message by the specified amount and print the resulting encoded or decoded message to the console.

## Examples
```py
$ python ceaser_cipher.py
Type 'encode' to encrypt or type 'decode' to decrypt
encode
Type your message below
hello world
Enter a shift number
2
Here is the encoded result: jgnnq yqtnf
Copy code
$ python ceaser_cipher.py
Type 'encode' to encrypt or type 'decode' to decrypt
decode
Type your message below
jgnnq yqtnf
Enter a shift number
2
Here is the decoded result: hello world
```

## Note
+ This program is using an imported module alphabets and art that contains the alphabets list and the logo art respectively.
+ A test version of this program is available on [replit.](https://replit.com/@labelisaiah/caesar-cipher-encryption-and-decryption?v=1) Feel free to test it out and give feedback for improvements.
+ Also, this program creates a loop that allows user to keep running the program as long as they want.

## Requirements
+ Python 3.x
+ import module alphabets and art

## Dependencies
This program has two dependencies alphabets and art modules, that should be available in the same directory as the ceaser_cipher.py file.

## Limitations
+ The program does not handle upper case letters, special characters and digits.
+ The program assumes that the user will input valid integers for the shift number.

## Contributions
This program is part of my learning project. Contributions and suggestions for improvements are welcome. If you would like to contribute to the development of this program, please fork the repository and submit a pull request with your proposed changes.

## License
This program is licensed under the *MIT License.*

## Acknowledgements
I would like to thank Dr. Angela Yu who has helped improve my understanding of Python and the Ceaser Cipher algorithm.

Thank you for using Ceaser Cipher.
