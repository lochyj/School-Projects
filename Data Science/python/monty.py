import random

def monty_hall():
    doors = [1, 2, 3]
    car = random.choice(doors)
    choice = random.choice(doors)

    if choice == car:
        return True
    else:
        return False

def main():
    results = []
    for _ in range(1, 300000):
        results.append(monty_hall())
    switch = results.count(False)
    stay = results.count(True)

    print(f"Switching wins: {switch}")
    print(f"Staying wins: {stay}")

main()