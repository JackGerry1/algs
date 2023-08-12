def caesar_cipher(text, shift, decrypt=False):
    result_text = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shift_amount = shift if not decrypt else -shift
            decrypted_char = chr(
                (ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
            result_text += decrypted_char
        else:
            result_text += char

    return result_text


def main():
    while True:
        try:
            choice = input("Encrypt or Decrypt? (e/d): ").lower()
            if choice not in ['e', 'd']:
                raise ValueError("Invalid choice. Please enter 'e' or 'd'.")

            text = input("Enter the text: ")
            shift = int(input("Enter the shift value (integer): "))
            if not isinstance(shift, int):
                raise ValueError(
                    "Invalid shift value. Please enter an integer.")

            if choice == 'e':
                encrypted_text = caesar_cipher(text, shift)
                print("Encrypted text:", encrypted_text)
            else:
                decrypted_text = caesar_cipher(text, shift, decrypt=True)
                print("Decrypted text:", decrypted_text)

            break  # Exit the loop if input is valid

        except ValueError as e:
            print(f"Error: {e}. Please try again.")


if __name__ == "__main__":
    main()
