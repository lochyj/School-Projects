# for i in range(1, 100):
#     if i % 15 == 0:
#         print("fizz-buzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)

# print(input("Input: ")[::-1])

# print("The quick brown fox jumped over the lazy dog"[::-1])

# s = input("Enter string: "); c = input("Enter character: ")[0]
# if c in s:
#     for i, char in enumerate(s):
#         if char == c:
#             print(f"Character found at index [{i + 1}]")
#             break
# else:
#     print("Character isn't present in the string provided")

# print(sum(range(1, 1001)))

# palindrome = input("Enter a word to be checked if it is a palindrome: ")

# print(palindrome == palindrome[::-1])

for i in range (0, 2**7):
    print(f"Bin: {bin(i).split('b')[1]}, Decimal: {i}")
