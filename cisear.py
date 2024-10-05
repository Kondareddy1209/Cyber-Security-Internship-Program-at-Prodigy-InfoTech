def encrypt_caesar(plaintext, shift):
    encrypt_text = ""
    for char in plaintext:
        if char.isupper():
            encrypt_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypt_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypt_text += char
    return encrypt_text

def decrypt_caesar(ciphertext, shift):
    decrypt_text = ""
    for char in ciphertext:  
        if char.isupper():
            decrypt_text += chr((ord(char) - shift - 65) % 26 + 65)  
        elif char.islower():
            decrypt_text += chr((ord(char) - shift - 97) % 26 + 97) 
        else:
            decrypt_text += char  
    return decrypt_text

def main():
    choice=input("(E)Encryption or (D)Decryption :  ").upper()
    message = input("Enter the message : ")
    shift = int(input("Enter the shift value: "))


    shift = shift % 26
    
    if choice == 'E':
        encrypt_message = encrypt_caesar(message,shift)
        print("encrypted message: ",encrypt_message)
    elif choice == 'D':
        decrypt_message = decrypt_caesar(message , shift)
        print("decrypt message :",decrypt_message)
    else:
        print("Invalid choice please selcect correct choice.")

if __name__ == "__main__":
    main()
