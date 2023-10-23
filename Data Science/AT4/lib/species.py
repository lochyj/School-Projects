class Species:
    def __init__(self, initial_population):
        self.pop = initial_population

    def eat(self):
        if self.pop < 1:
            return False

        self.pop -= 1
        return True
    
    def tick(self):
        ...
