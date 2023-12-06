import keyboard
from pynput.keyboard import Key, Listener

print("Here you can choose which characters you are going to encrypt:")

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result



def decrypt(text, shift):
    return encrypt(text, -shift)

# Exemple d'utilisation
text_to_encrypt = input()
shift_value = 3

#keyboard.is_pressed("²")


encrypted_text = encrypt(text_to_encrypt, shift_value)
print(f"Encrypted text : {encrypted_text}")


while True:
    print("Press 1 to decrypt your input or press 2 to enter a new value to encrypt. Press 3 to quit the application")
    choice = input("Your choice: ")

    if choice == "1":
        decrypted_text = decrypt(encrypted_text, shift_value)
        print(f"Decrypted text: {decrypted_text}")
    
    elif choice == "2":
        text_to_encrypt = input("Enter the text to encrypt: ")
        print("select a Shift value for the algorithm")
        shift_value = int(input(""))
        encrypted_text = encrypt(text_to_encrypt, shift_value)
        print(f"Encrypted text: {encrypted_text}")
    
    elif choice == "3":
        print("The key '3' was pressed. Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter '1' to decrypt or '2' to quit.")

    

    