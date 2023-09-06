for i in reversed(range(1, 11)):
    for _ in range(0, 2):
        print(f"{i} green bottle{'' if i == 1 else 's'} hanging on the wall,")
    print("And if one green bottle should accidentally fall,")
    print(f"There'll be {(i - 1) if i - 1 != 0 else 'no'} green bottles hanging on the wall.\n")