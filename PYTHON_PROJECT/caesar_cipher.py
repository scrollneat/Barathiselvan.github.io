alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

question1 = input("Type 'encode' to Encrypt and 'decode' to Decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift_number = int(input("Type the Shift number:\n"))

def encrypt(original_text, shift_num):
    encrypt_text = ''
    for i in range(len(text)):
        position = alphabets.index(text[i])
        shift_position = position + shift_num
        if shift_position <= 25:
            encrypt_text += alphabets[shift_position]
        else:
            out_of_range_position = shift_position - 26
            encrypt_text += alphabets[out_of_range_position]
    print(encrypt_text)

encrypt(text, shift_number)

