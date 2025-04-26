def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    if mode == 'decrypt':
        shift = -shift  # reverse the shift for decryption

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char  # leave non-alphabet characters unchanged

    return result

def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").strip().lower()

    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'E' or 'D'.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (e.g., 3): "))
    except ValueError:
        print("Shift value must be an integer.")
        return

    if choice == 'e':
        encrypted = caesar_cipher(message, shift, mode='encrypt')
        print("Encrypted message:", encrypted)
    else:
        decrypted = caesar_cipher(message, shift, mode='decrypt')
        print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
