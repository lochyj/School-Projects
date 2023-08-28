year = input("Enter year: ")

if int(year) % 4 == 0 and not(int(year[:2]) % 4 == 0 and int(year[2:]) == 0):
    print("its a leap year...")

