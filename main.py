from random import randint

# new_matrix = [[matrix[i][j] ^ key_matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
# output = ''.join([chr(int(''.join(map(str, row)), 2)) for row in new_matrix])

# input = input("Enter the text to encrypt: ")
# input = """"""
key = ''.join(chr(randint(33, 126)) for _ in range(len(input)))
matrix = [[int(bit) for bit in f"{bin(ord(chr))[2:]:0>8}"] for chr in [*input]]
key_matrix = [[int(bit) for bit in f"{bin(ord(chr))[2:]:0>8}"] for chr in [*key]]
output = ''.join([chr(int(''.join(map(str, row)), 2)) for row in [[matrix[i][j] ^ key_matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]])
print(output + "\nKey: " + key)


# Decrypt:

# input = input("Enter the text to decrypt: ")
# key = input("Enter the key: ")
# input = output
# key = key
# matrix = [[int(bit) for bit in f"{bin(ord(chr))[2:]:0>8}"] for chr in [*input]]
# key_matrix = [[int(bit) for bit in f"{bin(ord(chr))[2:]:0>8}"] for chr in [*key]]
# output = ''.join([chr(int(''.join(map(str, row)), 2)) for row in [[matrix[i][j] ^ key_matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]])
# print(output)
