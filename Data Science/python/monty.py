import random

def monty_hall():
    doors = [1, 2, 3]
    car = random.choice(doors)
    choice = random.choice(doors)

    if choice == car:
        return True

    return False

def main():
    results = []
    total = 1000000
    for i in range(1, total):
        results.append(monty_hall())
        print(f"Iter: {i}", end='\r')
    loose = results.count(False)
    win = results.count(True)

    print(f"You won {win / total * 100}% of the time.")
    print(f"You lost {loose / total * 100}% of the time.")


main()