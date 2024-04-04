from random import randint

# Encrypt:
def encrypt(input: str):
    try:
        key = ''.join(chr(randint(33, 126)) for _ in range(len(input)))
        matrix = [[int(bit) for bit in f"{bin(ord(chr))[2:]:0>8}"] for chr in [*input]]
        key_matrix = [[int(bit) for bit in f"{bin(ord(chr))[2:]:0>8}"] for chr in [*key]]
        output = ''.join([chr(int(''.join(map(str, row)), 2)) for row in [[matrix[i][j] ^ key_matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]])
        return output, key
    except Exception as e:
        return False

# Decrypt:
def decrypt(input: str, key: str):
    try:
        matrix = [[int(bit) for bit in f"{bin(ord(chr))[2:]:0>8}"] for chr in [*input]]
        key_matrix = [[int(bit) for bit in f"{bin(ord(chr))[2:]:0>8}"] for chr in [*key]]
        output = ''.join([chr(int(''.join(map(str, row)), 2)) for row in [[matrix[i][j] ^ key_matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]])
        return output
    except Exception as e:
        return False


while True:
    user_input = input("Enter 'e' to encrypt or 'd' to decrypt: ")

    if user_input == "e":
        input_text = input("Enter text to encrypt: ")
        encrypted_text, key = encrypt(input_text)
        if not encrypted_text:
            print("Error encrypting text")
            continue
        print(f"Encrypted text: {encrypted_text}")
        print(f"Key: {key}")

    elif user_input == "d":
        input_text = input("Enter text to decrypt: ")
        key = input("Enter key: ")
        decrypted_text = decrypt(input_text, key)
        if not decrypted_text:
            print("Error decrypting text")
            continue
        print(f"Decrypted text: {decrypted_text}")

    else:
        break