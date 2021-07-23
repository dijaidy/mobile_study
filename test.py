class animal:
    animal_kind = 0

    def __init__(self):
        self.weight = 50

    def function(self):
        animal.animal_kind = self
        animal.animal_kind.weight = 100


class pig(animal):
    def __init__(self):
        self.weight = 50

    def __str__(self):
        return "weight:" + str(self.weight)


pluf = pig()
pluf.function()

print(pluf)
