import datetime
import calendar

class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        if not self.checkValid():
            print("Date is invalid")
            self.day = 1
            self.month = 1
            self.year = 1

    def checkValid(self) -> bool:
        try:
            # This is the easy way of checking if a date is valid
            datetime.datetime(year=self.year, month=self.month, day=self.day)
            return True
        except:
            return False

    def isLeapYear(year: int):
        return calendar.isleap(year)

    def daysInMonth(self, month: int) -> int | None:
        try:
            return calendar.monthrange(2000, month)[1] # Returns a tuple with (<something useless>, <days in month>)
        except:
            return None

class Food:
    def __init__(self, name: str, servingSize: float):
        self.name: str = name
        self.servingSize: float = servingSize

    def __str__(self) -> str:
        self.print()

    def print(self):
        print("- Food -")
        print(f"Name: {self.name}")
        print(f"Name: {self.servingSize:.2f}")
        print("- Food -")

class Monster:
    def __init__(self, name: str):
        self.name = name
        self.birthday = Date(10, 4, 2000)
        self.canFly: bool = False
        self.nLegs: int = 0
        self.nEyes: int = 0
        self.favouriteFood: Food = Food("Sushi", 2.43)
        self.amountEaten: float = 1.0
        self.personality = "Angry"

    def eat(self, serves: int) -> float:

        serving_size = self.favouriteFood.servingSize

        consumed_food = serving_size * serves # Get the amount of food in kgs that the monster will eat
        self.amountEaten += consumed_food # Add the amount to total eaten

        return consumed_food

    def looseLimb(self) -> bool:
        if self.nLegs > 0:
            self.nLegs -= 1
            return True

        return False

    def looseEye(self) -> bool:
        if self.nEyes > 0:
            self.nEyes -= 1
            return True

        return False

    def __str__(self) -> str:
        self.print()

    def print(self):
        print("---------")
        print(f"Name: {self.name}")
        print(f"Can Fly: {self.canFly}")
        print(f"# Eyes: {self.nEyes}")
        print(f"# Legs: {self.nLegs}")
        self.favouriteFood.print()
        print(f"Personality: {self.personality}")
        print(f"Birthday: Y: {self.birthday.year}; M: {self.birthday.month}; D: {self.birthday.day};")
        print("---------")

class Zoo:
    def __init__(self):
        self.monsters: list[Monster] = []
        self.numMonsters: int = 0
        self.maxCapacity: int = 0

    def add(self, monster: Monster) -> bool:
        if self.maxCapacity == self.numMonsters:
            return False

        self.monsters.append(monster)
        self.numMonsters += 1

    def remove(self, name: str) -> bool:

        monster_index = self.find(name)
        self.monsters.pop(monster_index)

        return True

    def find(self, name: str) -> int | None:
        # Iterate over each monster and check if the monster has the name we are looking for.
        # Suppose we done have multiple monsters with the same name
        for i, monster in enumerate(self.monsters):
            if monster.name == name:
                return i
        return None

    def printMonster(self, name: str):
        idx = self.find(name) # Get the index of the monster with the name <name>
        if idx == None:
            print(f"Could not find monster '{name}'") # Uhhhhhh... This is awkward

        monster = self.monsters[idx]

        monster.print()

    # Removes and returns the monster from the zoo
    def getMonster(self, idx: int) -> Monster | None:
        if idx > self.numMonsters:
            return None

        monster = self.monsters[idx]

        self.monsters.pop(idx)

        return monster

    def __str__(self) -> str:
        self.printAllMonsters()

    def printAllMonsters(self):
        for monster in self.monsters:
            monster.print()

# --------|
# Testing |:
# --------|

zoo = Zoo()

zoo.maxCapacity = 10

zoo.add(Monster("Jim"))
zoo.add(Monster("Bob"))
zoo.printAllMonsters()
print(zoo.find("Jim")) # -> 0
print(zoo.find("Bob")) # -> 0
Jim = zoo.getMonster(zoo.find("Jim"))
Jim.name = "Uh Oh"

print(f"Does jim have a real birthday? {Jim.birthday.checkValid()}")

zoo.add(Jim)

del Jim
zoo.printMonster("Uh Oh")
