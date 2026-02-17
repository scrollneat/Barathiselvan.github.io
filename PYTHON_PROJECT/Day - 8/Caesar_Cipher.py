import ascii_art

print(ascii_art.caesar_cipher_logo)
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_num, function):
        secret_text = ''
        if function == "decode":
            shift_num *= -1
        for i in range(len(original_text)):
            if original_text[i] not in alphabets:
                secret_text += original_text[i]
            else:
                position = alphabets.index(original_text[i])

                

                shift_position = position + shift_num
                shift_position %= len(alphabets)
                secret_text += alphabets[shift_position]
        print(f"Here is your {function}d Text, There is no secret in this world!: {secret_text}")
        


go_continue = True
while go_continue:
    question1 = input("Type 'encode' to Encrypt and 'decode' to Decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift_number = int(input("Type the Shift number:\n"))

    caesar(original_text = text, shift_num = shift_number, function = question1)

    go_ahead = input("Type 'yes' if you want to go again or Type 'no' to exit:\n ").lower()

    if go_ahead == "yes":
         go_continue = True
    elif go_ahead == 'no':
         go_continue = False
         print('Good Bye!')




# def encrypt(original_text, shift_num):
#     encrypt_text = ''
#     for i in range(len(text)):
#         position1 = alphabets.index(text[i])
#         shift_position1 = position1 + shift_num
#         shift_position1 %= len(alphabets)
#         encrypt_text += alphabets[shift_position1]
#         # if shift_position1 <= 25:
#         #     encrypt_text += alphabets[shift_position1]
#         # else:
#         #     out_of_range_position = shift_position1 - 26
#         #     encrypt_text += alphabets[out_of_range_position]
#     print(f"Here is you Encrypted Text, Good Luck Cracking it!: {encrypt_text}")


# def decrypt(original_text, shift_num):
#     decrypt_text = ''
#     for i in range(len(text)):
#         position = alphabets.index(text[i])
#         shift_position = position - shift_num
#         shift_position %= len(alphabets)
#         decrypt_text += alphabets[shift_position]
#         # if shift_position <= 25:
#         #     decrypt_text += alphabets[shift_position]
#         # else:
#         #     out_of_range_position = shift_position - 26
#         #     decrypt_text += alphabets[out_of_range_position]
#     print(f"Here is you Decrypted Text, There is no secret in this world!: {decrypt_text}")
