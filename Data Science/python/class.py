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

# for i in range (0, 2**7):
#     print(f"Bin: {bin(i).split('b')[1]}, Decimal: {i}")

# import random

# results = []

# for i in range(100000):
#     test = []
#     for j in range(30):
#         test.append(random.choice([0, 1]))

#     results.append(test)

# total_heads = 0
# total_tails = 0

# longest_chain = 0

# for test in results:
#     current = 2
#     previous = 2

#     longest = 0

#     for val in test:
#         current = val

#         if current == previous:
#             longest += 1

#         elif current != previous:
#             longest = 0

#         match val:
#             case 0:
#                 total_heads += 1
#             case 1:
#                 total_tails += 1

#         previous = current

#     if longest > longest_chain:
#         longest_chain = longest

# total_flips = total_heads + total_tails

# print(f"Total heads: {total_heads}\nTotal tails: {total_tails}\nLongest sequence: {longest_chain}\nHeads percentage: {total_heads/total_flips*100}\nTails percentage: {total_tails/total_flips*100}")

x = 123456789.0
a = 101427
c = 321

m = 2**16

rand_list = []

for i in range(300):
    x = (a*x+c)%m
    random = x/m

    rand_list.append(round(random))

die_list = []

for i in range(0, 300, 10):
    roll = 0
    for j in range(1, 7):
        roll += rand_list[i + j]

    die_list.append(roll)

print(*die_list)
