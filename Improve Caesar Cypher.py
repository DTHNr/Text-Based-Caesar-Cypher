print(""" 
   _____                                  _____  _         _                 
  / ____|                                / ____|(_)       | |                
 | |       __ _   ___  ___   __ _  _ __  | |      _  _ __  | |__    ___  _ __ 
 | |      / _` | / _ \/ __| / _` || '__| | |     | || '_ \ | '_ \  / _ \| '__|
 | |____ | (_| ||  __/\__ \| (_| || |    | |____ | || |_) || | | ||  __/| |   
  \_____| \__,_| \___||___/ \__,_||_|     \_____||_|| .__/ |_| |_| \___||_|   
                                                    | |                       
                                                    |_|                                      
      """)




alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar_cipher(text, shift, encode_or_decode):
    shifted_text = ""
    if encode_or_decode == "decode":
        shift *= -1
    for letter in text:
        if letter == " ":
            shifted_text += letter
        else:
            original_index = alphabet.index(letter)
            new_index = (original_index + shift) % len(alphabet)
            shifted_text += alphabet[new_index]
    
    print(shifted_text)


should_continue = True

while should_continue:
    encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if encode_or_decode != "encode" and encode_or_decode != "decode":
        print("Your input is not among the choices!")
        continue

    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar_cipher(text, shift, encode_or_decode)

    try_again = input("Do you want to use Caesar Cipher again? Y/N: ").lower()
    if try_again == "n":
        print("Thank you for using the Caesar Cipher")
        should_continue = False

    